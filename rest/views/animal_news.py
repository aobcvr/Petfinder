from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest.serializer import AnimalNewsSerializer,UrlAnimalNewsSerializer


class AnimalNewsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UrlAnimalNewsSerializer

    def get(self, request):

        serializer = self.serializer_class(data=request.GET)
        serializer.is_valid(raise_exception=True)
        response = serializer.search_news()
        return Response(AnimalNewsSerializer(response, many=True).data)