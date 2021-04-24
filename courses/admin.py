from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'start_date', 'end_date', 'lecture_amount']
    list_display_links = ['id', 'title', 'author']
    list_filter = ['author', 'start_date', 'end_date']
    search_fields = ['title']
    list_per_page = 20
