from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts import views
from accounts.views import UserProfileViewSet

router = DefaultRouter()
router.register('users', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', obtain_auth_token),
    path('login/', views.UserLoginApiView.as_view()),
]

#
# urlpatterns = [
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('register/', views.register, name='register'),
#     path('edit_profile/', views.edit_profile, name='edit_profile'),
#
# ]
