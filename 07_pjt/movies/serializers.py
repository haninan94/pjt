from rest_framework import serializers
from .models import Movie, Actor, Review

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)

class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)



class ReviewNonIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

class ReviewSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Review
        fields = ('id', 'title', 'content',)
        read_only_fields = ('movie',)



class MovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):

    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'movies', 'name',)



class MovieSerializer(serializers.ModelSerializer):
    
    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReviewNonIdSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path',)