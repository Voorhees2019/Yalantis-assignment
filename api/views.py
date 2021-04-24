from .serializers import CoursesSerializer, CourseSerializer
from courses.models import Course
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()
            token = Token.objects.get(user=user).key
            return JsonResponse({'token': token}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'That username has already been taken. '
                                          'Please choose a new username'}, status=400)


class CourseListCreate(generics.ListCreateAPIView):
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'start_date', 'end_date']

    def get_queryset(self):
        return Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Course.objects.all()

    def perform_update(self, serializer):
        course = Course.objects.filter(pk=self.kwargs['pk'], author=self.request.user)
        if course.exists():
            serializer.save()
            return
        raise ValidationError('This isn\'t your course to update!')

    def delete(self, request, *args, **kwargs):
        course = Course.objects.filter(pk=self.kwargs['pk'], author=self.request.user)
        if course.exists():
            return self.destroy(request, *args, **kwargs)
        raise ValidationError('This isn\'t your course to delete!')
