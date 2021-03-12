from rest_framework.response import Response
from rest_framework.views import APIView

from sharing_code.models import Snippet
from .serializers import SnippetSerializer


class SnippetAPIView(APIView):

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        snippet = Snippet.objects.get(pk=kwargs['pk'])
        serializer = SnippetSerializer(instance=snippet)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset, many=True)
        return Response(serializer.data)