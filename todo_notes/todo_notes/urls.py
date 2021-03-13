from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views import AuthorModelViewSet
from todo_app.views import ProjectModelViewSet, TODOModelViewSet

router = DefaultRouter()
router.register('employees', AuthorModelViewSet)
router.register(r'projects', ProjectModelViewSet, basename='Project')
router.register(r'todos', TODOModelViewSet, basename='TODO')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
