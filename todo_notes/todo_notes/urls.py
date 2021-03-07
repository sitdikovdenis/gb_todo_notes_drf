from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import AuthorModelViewSet

router = DefaultRouter()
router.register('employees', AuthorModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
]
