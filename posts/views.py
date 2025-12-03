from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime
from django.utils import timezone

@api_view(['GET'])
def time_info(request):
    now = timezone.now()

    data = {
        'time': now.strftime('%H:%M:%S'),
        'date': now.strftime('%Y-%m-%d'),
        'weekday': now.weekday(),
    }
    return Response(data)

@api_view(['GET'])
def greeting(request):
    now = timezone.now()
    hour = now.hour

    text = ''

    if 5 <= hour < 12:
        text = 'Good Morning'
    elif 12 <= hour < 18:
        text = 'Good Afternoon'
    elif 18 <= hour < 24:
        text = 'Good Evening'

    data = {
        'time': now.strftime('%H:%M:%S'),
        'greeting': text,
    }
    return Response(data)

@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all().order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def comment_detail(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)