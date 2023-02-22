from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('service.urls')),
    path('web_lib', include('web_lib.urls')),
    path('admin/', admin.site.urls),
]
