from gc import get_objects

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.tasks.models import Tag
from apps.tasks.serializers.tag_serializer import TagSerializer


class TagView(APIView):
    def get(self, request):
        tags = self.get_objects()
        if not tags.exists():
            return Response({'error': 'No tags found'}, status=status.HTTP_204_NO_CONTENT)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_objects(self):
        return Tag.objects.all()


    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)