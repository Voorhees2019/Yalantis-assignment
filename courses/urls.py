from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    path('about/', views.about, name='about'),
    path('searchresult/', views.searchresult, name='searchresult'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course-delete'),

]
