from django.urls import path,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'snippers', views.SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]