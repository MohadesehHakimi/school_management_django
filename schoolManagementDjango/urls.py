from django.contrib import admin
from django.urls import path, include

from school_management import (urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('api_auth/', include('rest_framework.urls')),
]
