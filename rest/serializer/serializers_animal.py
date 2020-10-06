from listanimal.models import AnimalInfo, AnimalColor, AnimalType, Comment
from rest_framework import serializers


class AnimalTypeSerializer (serializers.ModelSerializer):
    '''
    Сериализует все объекты объявленией животных
    '''
    class Meta:
        model = AnimalType
        fields='__all__'


class AnimalColorSerializer (serializers.ModelSerializer):
    '''
    Сериализует все цвета животных
    '''
    primary = serializers.CharField(max_length=200)

    class Meta:
        model = AnimalColor
        fields = '__all__'


class AnimalInfoSerializer(serializers.ModelSerializer):
    color = AnimalColorSerializer()
    animal_type = AnimalTypeSerializer()
    id = serializers.ReadOnlyField()

    class Meta:
        model = AnimalInfo
        fields = '__all__'


class CommentSerializer (serializers.ModelSerializer):
    '''
    Сериализует все объекты комментариев к животным
    '''
    class Meta:
        model = Comment
        fields = '__all__'