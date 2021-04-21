from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['user_name', 'first_name', 'last_name']


class AuthorModelSerializer20(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['user_name', 'first_name', 'last_name', 'email', 'url', 'birthday_year']


class AuthorModelInTODOAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['user_name', 'first_name', 'last_name', 'email', 'birthday_year', 'url']
