from django.contrib import admin
from django.urls import path
from client.views import ClubConsultingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clubconsulting/', ClubConsultingView.as_view())
]
