from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    if request.user.is_authenticated:
        return redirect('courses')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created.')
            # login after registration
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('courses')
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
