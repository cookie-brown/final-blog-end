from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from articles.serializers import UserSerializer, ArticleSerializer
# Model引入
from django.contrib.auth.models import User
from .models import Article


# 获取文章列表
@api_view(['GET'])
def get_articlesList_view(request):
    querysets = Article.objects.all()
    print(querysets)
    print(querysets.values())
    querysetsList = querysets.values()
    articlesList = []
    for item in querysetsList:
        article = {
            'articleId': item['id'],
            'title': item['title'],
            'imageSrc': item['cover'],
            'createTime': item['created_time'],
            'updateTime': item['updated_time'],
            'readTime': item['read_times']
        }
        articlesList.append(article)
    articlesList=articlesList[::-1]
    return Response({'articlesList': articlesList})    