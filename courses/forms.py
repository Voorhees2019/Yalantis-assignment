from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local', }), required=False)
    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local', }), required=False)

    class Meta:
        model = Course
        exclude = ('author', )
