# from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets

from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
