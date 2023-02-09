from django.contrib import admin
from django.urls import path, include
from knox import views as knox_views
from accounts.views import RegisterAPI, LoginAPI, ChangePasswordView
from client.views import ClubConsultingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/clubconsulting/', ClubConsultingView.as_view())
]
