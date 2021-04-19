from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter, TODOFilter
from .models import Project, TODO
from .serializers import ProjectModelSerializer, TODOModelSerializer, TODOModelWithAuthorSerializer, TODOModelSerializerList


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(users=self.request.data.get('users'))


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filterset_class = TODOFilter
    # permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        partial = kwargs.pop('partial', True)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance.state = 'C'
        instance.save()
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(project=self.request.data.get('project'))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_context = {
            'request': request,
        }

        serializer_class = TODOModelSerializerList
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = serializer_class(page, many=True, context=serializer_context)
            return self.get_paginated_response(serializer.data)

        serializer = serializer_class(queryset, many=True, context=serializer_context)
        return Response(serializer.data)


class TODOModelViewSet2(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelWithAuthorSerializer
    permission_classes = [permissions.IsAuthenticated]
