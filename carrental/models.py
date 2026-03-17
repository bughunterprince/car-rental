from django.contrib.auth.models import User
from django.db import models


class FaceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="face_profile")
    face_encoding = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"FaceProfile<{self.user.username}>"
