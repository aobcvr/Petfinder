from rest_framework import serializers
from django.db.models import Q
from listanimal.models import AnimalInfo,AnimalColor,AnimalType

class UrlAnimalAdvertSerializer(serializers.Serializer):
    size=serializers.ChoiceField(default=None,choices=[('Large','Large'),('Medium','Medium'),('Small','Small')])
    color=serializers.SlugRelatedField(default=None,queryset=AnimalColor.objects.all(),slug_field='primary',many=True)
    animaltype=serializers.PrimaryKeyRelatedField(default=None,queryset=AnimalType.objects.all(),many=True)

    def search_advert(self):
        data=self.validated_data
        val=Q()
        if data['size'] is not None:
            val &= Q(size=self.validated_data['size'])
        if data['color']  !=[]:
            val &= Q(color__in=self.validated_data['color'])
        if data['animaltype'] != []:
            val &=Q(animal_type__in=self.validated_data['animaltype'])
        return AnimalInfo.objects.filter(val)


