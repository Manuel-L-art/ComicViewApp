from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        user = User.objects.register(request.POST)
        request.session['user_id'] = user.id
        messages.success(request, "Successful Registration")
    return render(request, 'dashboard.html')

def login(request):
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, "Email and Password combination does not match records")
        return redirect('/')
    user = User.objects.filter(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "Logging in")
    return render(request, 'dashboard.html')

def logout(request):
    request.session.clear()
    return redirect('')

# def edit(request):
#     # user changes password
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()    
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else: 
#         form = PasswordChangeForm(request.user)
#         return render(request, 'accounts/change_password.html', {
#             'form': form
#         })
#     return redirect('/')

def add_comment(request):
    user = request.user
    Comment.objects.create(
        comment = request.POST['comments'],
        user = user.id
    )
    return redirect('/')