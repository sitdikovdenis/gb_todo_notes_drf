import graphene
from graphene_django import DjangoObjectType
from library.models import Author
from todo_app.models import TODO, Project


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)

    def resolve_all_authors(root, info):
        return Author.objects.all()

    all_todos = graphene.List(TODOType)

    def resolve_all_todos(root, info):
        return TODO.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()


schema = graphene.Schema(query=Query)
