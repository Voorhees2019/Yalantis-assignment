from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    lecture_amount = models.IntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})

    def clean(self):
        if self.start_date and self.end_date:
            if self.end_date <= self.start_date:
                raise ValidationError('End date must be greater than start date.')
        if self.start_date:
            if self.start_date < timezone.now():
                raise ValidationError('Start date must be greater than current time.')
        if self.lecture_amount:
            if self.lecture_amount < 1:
                raise ValidationError('Lecture amount must be greater than 0')

    class Meta:
        ordering = ['start_date']
