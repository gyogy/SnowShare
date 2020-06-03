from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('rides/', include('rides.urls')),
    path('admin/', admin.site.urls),
]
