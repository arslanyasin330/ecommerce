from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views
from accounts.views import UserProfileViewSet

router = DefaultRouter()
router.register('users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
