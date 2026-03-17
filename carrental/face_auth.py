import base64
import json
from io import BytesIO
from typing import Optional

import cv2
import numpy as np
from PIL import Image

_CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
_FACE_CASCADE = cv2.CascadeClassifier(_CASCADE_PATH)


def is_face_ai_available() -> bool:
    return _FACE_CASCADE is not None and not _FACE_CASCADE.empty()


def _image_from_data_url(data_url: str):
    if "," not in data_url:
        return None

    try:
        _, encoded = data_url.split(",", 1)
        raw = base64.b64decode(encoded)
        image = Image.open(BytesIO(raw)).convert("RGB")
        return np.array(image)
    except Exception:
        return None


def extract_face_encoding_from_data_url(data_url: str) -> Optional[np.ndarray]:
    if not is_face_ai_available():
        return None

    image_array = _image_from_data_url(data_url)
    if image_array is None:
        return None

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    faces = _FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80),
    )
    if len(faces) == 0:
        return None

    # Use the largest detected face to reduce background noise.
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    face_roi = gray[y : y + h, x : x + w]
    face_roi = cv2.resize(face_roi, (128, 128), interpolation=cv2.INTER_AREA)

    encoding = face_roi.astype(np.float32).flatten() / 255.0
    norm = np.linalg.norm(encoding)
    if norm == 0:
        return None

    return encoding / norm


def encoding_to_text(encoding: np.ndarray) -> str:
    return json.dumps(encoding.tolist())


def text_to_encoding(payload: str) -> Optional[np.ndarray]:
    try:
        values = json.loads(payload)
        return np.array(values, dtype=np.float64)
    except Exception:
        return None


def match_face_encoding(stored_encoding: np.ndarray, probe_encoding: np.ndarray, tolerance: float = 0.5) -> bool:
    if stored_encoding is None or probe_encoding is None:
        return False

    # Cosine similarity threshold for the normalized OpenCV encoding.
    score = float(np.dot(stored_encoding, probe_encoding))
    return score >= max(0.86, 1.0 - tolerance)
