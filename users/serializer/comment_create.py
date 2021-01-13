from users.models.comment import Comment
from listanimal.models.animal_info import AnimalInfo
from listanimal.models.animal_news import AnimalNews

from rest_framework import serializers


class CreateCommentSerializer(serializers.Serializer):

    type = serializers.ChoiceField(choices=[('news', 'news'), ('animal', 'animal')])
    id_object = serializers.IntegerField(min_value=1)
    comment = serializers.CharField(max_length=100)

    def create(self, request):
        validated_data = self.validated_data
        user = request.user
        print(validated_data['type'])
        if validated_data['type'] == 'animal':
            object = AnimalInfo.objects.get(id=validated_data['id_object'])
            print(object)
            Comment.objects.create(content_object=object,
                                   comment=validated_data['comment'],
                                   user=user,
                                   object_id=validated_data['id_object'])
        if validated_data['type'] == 'news':
            object = AnimalNews.objects.get(id=validated_data['id_object'])
            print(object)
            Comment.objects.create(content_object=object,
                                   comment=validated_data['comment'],
                                   user=user,
                                   object_id=validated_data['id_object'])
        return object
