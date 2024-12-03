from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'date_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'genre', 'movie_image',
                  'movie_status', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class MovieMomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    movieLanguages = MovieLanguagesSerializer(many=True, read_only=True)
    movie_moments = MovieMomentsSerializer(many=True, read_only=True)
    comments = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'genre', 'director', 'actor', 'movie_image', 'movie_trailer',
                 'types', 'movie_status', 'movie_time', 'movieLanguages', 'movie_moments', 'comments']
