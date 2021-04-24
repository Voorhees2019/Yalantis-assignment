from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Accounts
    path('accounts/', include('accounts.urls')),
    # Courses
    path('', include('courses.urls')),
    # API
    path('api/', include('api.urls')),
]
