# from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets

from .models import Author
from .serializers import AuthorModelSerializer, AuthorModelSerializer20


class AuthorModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return AuthorModelSerializer20

        return AuthorModelSerializer
