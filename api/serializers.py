from rest_framework.serializers  import ModelSerializer

from .models import Genre, Movie

class GenreSerializer(ModelSerializer):
    class Meta:
        model=Genre
        fields=['name',]


class MovieSerializer(ModelSerializer):
    class Meta:
        model=Movie 
        fields='__all__'