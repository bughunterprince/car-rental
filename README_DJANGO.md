# Django Backend + AI Face Login

## 1) Install dependencies

```bash
pip install -r requirements.txt
```

## 2) Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 3) Start server

```bash
python manage.py runserver
```

## 4) Use system

- Open `http://127.0.0.1:8000/register/`
- Register user and click `Capture Face For Login`
- Open `http://127.0.0.1:8000/login/`
- Use either password login or `Login With Face`

## Notes

- Face login uses webcam capture in browser and server-side matching with `face_recognition`.
- If `face_recognition` install fails on Windows, install Visual C++ Build Tools and retry.
- Dashboard routes are protected with Django sessions.
