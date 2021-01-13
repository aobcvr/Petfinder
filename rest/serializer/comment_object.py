from rest_framework import serializers

from listanimal.models import AnimalInfo, AnimalNews

from users.models.comment import Comment
from django.contrib.contenttypes.models import ContentType


class CommentObject(serializers.Serializer):

    content_type = serializers.ChoiceField(choices=[('news', 'news'), ('animal', 'animal')])
    object_id = serializers.IntegerField(min_value=1)

    def comment_object(self):
        validated_data = self.validated_data
        if validated_data['content_type'] == 'animal':
            object = AnimalInfo.objects.get(id=validated_data['object_id'])
            object_type = ContentType.objects.get_for_model(object)
            comment = Comment.objects.filter(content_type__pk=object_type.id, object_id=object.id)
        if validated_data['content_type'] == 'news':
            object = AnimalNews.objects.get(id=validated_data['object_id'])
            object_type = ContentType.objects.get_for_model(object)
            comment = Comment.objects.filter(content_type__pk=object_type.id, object_id=object.id)
        return comment
