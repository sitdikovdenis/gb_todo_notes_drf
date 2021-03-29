from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from library.views import AuthorModelViewSet
from todo_app.views import ProjectModelViewSet, TODOModelViewSet, TODOModelViewSet2

router = DefaultRouter()
router.register('employees', AuthorModelViewSet)
router.register(r'projects', ProjectModelViewSet, basename='Project')
router.register(r'todos', TODOModelViewSet, basename='TODO')
router.register(r'api_todos', TODOModelViewSet2, basename='APITODO')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
