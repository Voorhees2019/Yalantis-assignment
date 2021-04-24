from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Courses
    path('courses/', views.CourseListCreate.as_view()),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroy.as_view()),
    # Auth
    path('signup/', views.signup),
    path('login/', obtain_auth_token),
]
