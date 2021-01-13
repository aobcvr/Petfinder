from users.models.comment import Comment

from rest_framework import serializers


class CommentSerializer (serializers.ModelSerializer):
    """
    Сериализует все объекты комментариев к животным
    """
    class Meta:
        model = Comment
        fields = '__all__'


