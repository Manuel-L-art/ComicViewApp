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
    return redirect('/loading')

def login(request):
    if not User.objects.authenticate(request.POST['email'], request.POST['pwd']):
        messages.error(request, "Email and Password combination does not match records")
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "Logging in")

    return redirect('/loading')

def renderDash(request):
    context = {
        "comics": Comic.objects.all(),
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

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

def allcommies(request, user_id):
    comments = Comment.objects.get(id=user_id)
    context = {
        "comments": comments,
    }
    return render(request, 'viewcommies.html', context)

def wip(request):
    return render(request, 'wip.html')

def submit(request):
    context = {
        "comics": Comic.objects.all(),
    }
    return render(request, 'submitComPag.html', context)

def createComic(request):
    com = Comic.objects.create(
        book_title = request.POST['book_title'],
        book_author = request.POST['book_author'],
        cover_art = request.FILES['cover_art'],
        release_date = request.POST['release_date'],
    )
    com.save()
    return redirect('/submit')

def submitPage(request):
    if request.method == 'POST':
        comInt = Comic.objects.get(id=request.POST['comicRef'])
        page = ComicPage.objects.create(
            page_no = request.POST['page_no'],
            comicRef = comInt,
            comic_img = request.FILES['comic_img'],
        )
        page.save()
    return redirect('/submit')

def viewComic(request, page_id):
    comicpage = ComicPage.objects.get(id=page_id)
    comments = Comment.objects.get(id=page_id)
    context = {
        "comicpage": comicpage,
        "comments": comments,
        
    }
    return render(request, 'view.html', context)

def addLikes(request, id):
    comment_liked = Comment.objects.get(id=id)
    liked_by = User.objects.get(id=request.session['id'])
    comment_liked.likes.add(liked_by)
    return redirect('/')

def bookmark(request,id):
    comicpage = ComicPage.objects.get(id=id)
    bookmarkedBy = User.objects.get(id=request.session['id'])
    comicpage.bookmarked.add(bookmarkedBy)
    return redirect('/viewComicPage<int:id>')