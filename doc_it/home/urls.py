from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserProfileViewSet, CategoryViewSet, DocumentViewSet, DocumentLogViewSet, AttachmentViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'document-logs', DocumentLogViewSet)
router.register(r'attachments', AttachmentViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("perguntasfrequentes", views.perguntasfrequentes, name="perguntasfrequentes"),
    path("funcionalidades", views.funcionalidades, name="funcionalidades"),

    path('api/', include(router.urls)),
]
