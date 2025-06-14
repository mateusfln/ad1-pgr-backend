from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class DocumentLog(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change_description = models.TextField()
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log for {self.document.title} by {self.user.username} on {self.changed_at}"


class Attachment(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.document.title}"
