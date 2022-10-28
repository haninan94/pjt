from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from .models import Movie, Actor, Review
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ActorListSerializer, ActorSerializer, MovieListSerializer, MovieSerializer, ReviewSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def actor_list(request):
    # 배우 목록 조회
    if request.method == 'GET':
        actors = get_list_or_404(Actor)
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    
    # 배우 생성
    if request.method == 'POST':
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def actor_detail(request, actor_pk):

    actor = get_object_or_404(Actor, pk=actor_pk)
    
    # 배우 조회
    if request.method == 'GET':
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    # 배우 삭제
    elif request.method == 'DELETE':
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 배우 정보 수정
    elif request.method == 'PUT':
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def movie_list(request):
    # 영화 목록 조회
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # 영화 생성
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)
    
    # 영화 조회
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # 영화 삭제
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 영화 정보 수정
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def review_list(request):

    if request.method == 'GET':
        # 리뷰 목록 조회
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    
    review = get_object_or_404(Review, pk=review_pk)

    # 리뷰 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 리뷰 삭제
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 리뷰 수정
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# 리뷰 생성
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    