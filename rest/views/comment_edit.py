from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from rest.serializer import CommentObject
from rest.serializer.comment_edit import CommentEdit
from users.models import Comment

class CommentEditView(viewsets.ViewSet):

    @action(methods=['post'], detail=True, permission_classes=['IsAuthenticated'])
    def create(self, request):
        serializer = CommentEdit(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.comment_edit(request)
        return Response(result)
