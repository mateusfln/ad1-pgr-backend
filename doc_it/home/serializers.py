from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Category, Document, DocumentLog, Attachment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'user_id', 'department', 'role', 'bio']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)  # Campo de input no POST/PUT

    class Meta:
        model = Document
        fields = '__all__'

class DocumentLogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    document = DocumentSerializer(read_only=True)
    document_id = serializers.IntegerField(write_only=True)


    class Meta:
        model = DocumentLog
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
