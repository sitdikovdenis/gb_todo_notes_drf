from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['user_name', 'first_name', 'last_name', 'email', 'url']
