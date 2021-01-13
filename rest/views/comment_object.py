from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets

from rest.serializer import CommentObject

from users.models import Comment
from rest.serializer import CommentSerializer


class CommentObjectView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = CommentObject(data=request.GET)
        serializer.is_valid(raise_exception=True)
        self.queryset = serializer.comment_object()
        return super().list(self, request, *args, **kwargs)
