from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerializer
from movies.models import Movie

# Creating api views
class Movieapilistview(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class Movieapiview(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'