from django.shortcuts import render, HttpResponse
from .forms import CourseForm
from .models import Course
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def about(request):
    return render(request, 'courses/about.html', {})


def searchresult(request):
    if request.GET.get('q'):
        query = request.GET.get('q', '')
        queries = query.strip().split(" ")
        search_result = []
        for q in queries:
            search_result += Course.objects.filter(title__icontains=q)
        return render(request, 'courses/search_result.html', {'query': query, 'search_result': search_result})
    else:
        return HttpResponse('Please submit a search form.')


class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'
    paginate_by = 10


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
