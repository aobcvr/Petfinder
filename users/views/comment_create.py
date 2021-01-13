from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from users.serializer import CreateCommentSerializer


class CommentViewSet(viewsets.ViewSet):

    @action(methods=['post'], detail=True, permission_classes=['IsAuthenticated'])
    def create(self, request):
        serializer = CreateCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(request)
        return Response({'status': 'comment was created'})
