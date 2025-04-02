from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('user/profile/', views.user_profile, name='user_profile'),

    # Rutas para JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtener token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refrescar token
]
