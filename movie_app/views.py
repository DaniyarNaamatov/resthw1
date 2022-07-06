from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import (
    DirectorSerializers,
    MovieSerializers,
    ReviewSerializers,
    DirectorValidateSerializer,
    MovieValidateSerializer,
    ReviewValidateSerializer,
)
from movie_app.models import Director, Movie, Review
from rest_framework import status
from django.contrib.auth.models import User
from movie_app.serializers import UserValidateSerializer, UserAuthorizationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class DirectorDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers
    lookup_field = 'id'




class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title']


class MovieDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'id'





class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['text']
    search_fields = ['text']


class ReviewDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers



@api_view(["GET"])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializers(movie_reviews, many=True).data
    return Response(data=data)





