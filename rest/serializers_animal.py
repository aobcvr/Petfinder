from listanimal.models import AnimalInfo,AnimalColor,AnimalType

from rest_framework import serializers

class AnimalTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields='__all__'

class AnimalColorSerializer (serializers.ModelSerializer):
    primary = serializers.CharField(max_length=200)

    class Meta:
        model = AnimalColor
        fields='__all__'


class AnimalInfoSerializer(serializers.ModelSerializer):
    color=AnimalColorSerializer()
    animal_type=AnimalTypeSerializer()
    id = serializers.ReadOnlyField()
    class Meta:
        model = AnimalInfo
        fields = '__all__'
