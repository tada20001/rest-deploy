from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.conf import settings
from django.conf.urls.static import static

app_name = 'api'

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
