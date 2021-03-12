from library.serializers import AuthorModelInTODOAppSerializer
from rest_framework import serializers

from .models import Project, TODO

from library.models import Author


class ProjectModelSerializer(serializers.ModelSerializer):
    users = AuthorModelInTODOAppSerializer(many=True)

    class Meta:
        model = Project
        fields = ['uuid', 'name', 'repository_url', 'users']


class TODOModelSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    project = ProjectModelSerializer()

    class Meta:
        model = TODO
        fields = '__all__'
