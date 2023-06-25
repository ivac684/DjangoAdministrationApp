from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def professor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'prof':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home') 
    return wrapper

def student_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'stu':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home') 
    return wrapper

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse('home')) 
    return wrapper
