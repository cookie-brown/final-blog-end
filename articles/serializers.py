from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'cover', 'content', 'markdown_content', 'created_time', 'updated_time', 'read_times')