from rest_framework import serializers
from courses.models import Course
from django.utils import timezone


class CoursesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Course
        fields = ['id', 'title', 'author', 'start_date', 'end_date', 'lecture_amount']


class CourseSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, required=False)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Course
        fields = ['id', 'title', 'author', 'start_date', 'end_date', 'lecture_amount']

    def validate(self, data):
        if 'start_date' in data and 'end_date' in data:
            if data['end_date'] <= data['start_date']:
                raise serializers.ValidationError('End date must be greater than start date.')
        if 'start_date' in data:
            if data['start_date'] < timezone.now():
                raise serializers.ValidationError('Start date must be greater than current time.')
        if 'end_date' in data:
            if data['end_date'] < timezone.now():
                raise serializers.ValidationError('End date must be greater than current time.')
        if 'lecture_amount' in data and data['lecture_amount'] < 1:
            raise serializers.ValidationError('Lecture amount must be greater than 0')
        return data
