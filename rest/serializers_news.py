from listanimal.models_news import AnimalNews
from rest_framework import serializers

class AnimalNewsSerializer(serializers.ModelSerializer):

        class Meta:
             model = AnimalNews
             fields = '__all__'

