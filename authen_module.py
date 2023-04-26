from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    context = {
        "login_view": "active"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "authen/login.html", context)

def logout_view(request):
  logout(request)
  return redirect("/")

# def signup_view(request):
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#         user = form.save()
#         user.refresh_from_db()
#         user.profile.first_name = form.cleaned_data.get('first_name')
#         user.profile.last_name = form.cleaned_data.get('last_name')
#         user.profile.email = form.cleaned_data.get('email')
#         user.profile.address = form.cleaned_data.get('email')
#         user.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

