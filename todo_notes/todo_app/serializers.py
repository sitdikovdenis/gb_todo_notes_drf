from library.serializers import AuthorModelInTODOAppSerializer
from rest_framework import serializers

from .models import Project, TODO

from library.models import Author


class ProjectModelSerializer(serializers.ModelSerializer):
    users = AuthorModelInTODOAppSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['uuid', 'name', 'repository_url', 'users']


class TODOModelSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = TODO
        fields = ['project', 'text', 'author']


class TODOModelSerializerList(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    project = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = '__all__'


class TODOModelWithAuthorSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='user_name', read_only=True)
    project = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = '__all__'
