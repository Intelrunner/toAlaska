from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('players/', include('players.urls')),
    path('admin/', admin.site.urls),
]
