from rest_framework import serializers

from django.db.models import Q

from listanimal.models import AnimalInfo, AnimalColor, AnimalType
from listanimal.enums import AnimalChoicesEnum


class UrlAnimalAdvertSerializer(serializers.Serializer):
    """
    выводит животных, которые попадают под фильтры
    """
    size = serializers.ChoiceField(default=None,
                                   choices=AnimalChoicesEnum.choices())
    color = serializers.SlugRelatedField(default=None,
                                         queryset=AnimalColor.objects.all(),
                                         slug_field='primary',
                                         many=True)
    animaltype = serializers.PrimaryKeyRelatedField(default=None,
                                                    queryset=AnimalType.objects.all(),
                                                    many=True)

    def search_advert(self):

        validated_data = self.validated_data
        val = Q()
        if validated_data['size'] is not None:
            val &= Q(size=validated_data['size'])
        if validated_data['color'] != []:
            val &= Q(color__in=validated_data['color'])
        if validated_data['animaltype'] != []:
            val &= Q(animal_type__in=validated_data['animaltype'])
        return AnimalInfo.objects.filter(val)
