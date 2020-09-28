from rest_framework import serializers
from django.db.models import Q
from listanimal.models import AnimalNews


class UrlAnimalNewsSerializer(serializers.Serializer):
    '''
    выводит новости в которых есть введенное предложение в search_line
    '''
    search_line = serializers.CharField()

    def search_news(self):
        queryset = AnimalNews.objects.filter(Q(description_news__contains=self.validated_data['search_line'])|
                                             Q(main_text__contains=self.validated_data['search_line'])|
                                             Q(heading__contains=self.validated_data['search_line']))
        return queryset