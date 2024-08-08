from .models import Artist, Albom, Song
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistSerializerMobile(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name')


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializerMobile()

    class Meta:
        model = Albom
        fields = ('id', 'title', 'artist')

class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer()
    class Meta:
        model = Song
        fields = ('id', 'title', 'image', 'albom')




