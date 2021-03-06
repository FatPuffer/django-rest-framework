from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics


class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, format=None):
        return self.list(queryset, **args, **kwargs)

    def post(self, request, format=None):
        return self.create


class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, pk, format=None):
        return self.retrieve(request, **args, **kwargs)

    def put(self, request, pk, format=None):
        return self.update(request, **args, **kwargs)

    def delete(self, request, pk, format=None):
        return self.destroy(request, **args, **kwargs)












