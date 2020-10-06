from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest.serializer import CommentSerializer

from listanimal.models import Comment


class CommentAnimal(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, pk):

        queriset = Comment.objects.filter(animal=pk)
        comments = CommentSerializer(queriset, many=True).data
        return Response(comments)