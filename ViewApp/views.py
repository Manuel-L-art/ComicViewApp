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
    comics = Comic.objects.all()
    context = {
        "comics": comics,
        # "pages": Comic.page.filter(
        #     comRef = comics.id
        # ),
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

def add_comment(request, book_title, page_no):
    comicpage = ComicPage.objects.get(
        comicRef = Comic.objects.get(book_title = book_title),
        page_no=page_no
    )
    comment = Comment.objects.create(
        comment = request.POST['comment'],
        name = request.POST['name'],
        pageRef = ComicPage.objects.get(id=comicpage.id)
    )
    comment.save()
    return redirect(f'/viewpage/{ book_title }/{page_no}')

def allcommies(request):
    comments = Comment.objects.all()
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

def viewPage(request, book_title, page_no):
    comicpage = ComicPage.objects.get(
        comicRef = Comic.objects.get(book_title=book_title),
        page_no=page_no,
    )
    
    comments = comicpage.pcomment.all()
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

# def bookmark(request,id):
#     comicpage = ComicPage.objects.get(id=id)
#     bookmarkedBy = User.objects.get(id=request.session['id'])
#     comicpage.bookmarked.add(bookmarkedBy)
#     return redirect('/viewComicPage<int:id>')

def delete(request):
    comics = Comic.objects.all()
    context = {
        "comics": comics,
    }
    return render(request, 'delete.html', context)

def deleteCom(request, id):
    com = Comic.objects.get(id=id)
    com.delete()
    return redirect('/delete')

def deletePage(request):
    comic_id = request.POST.get('comic_id', False)
    comic  = Comic.objects.get(id=comic_id)
    pages = comic.page.all()
    context = {
        "pages":pages,
        "comics": Comic.objects.all()
    }
    return render(request, 'delete.html', context)

def selectpage(request):
    page_id = request.POST.get('page_id', False)
    if page_id == False:
        return redirect('/delete')
    comicpage = ComicPage.objects.get(id=page_id)
    comicpage.delete()
    return redirect('/delete')

def nextPage(request, book_title, page_no):
    page_no = page_no + 1
    return redirect(f'/viewpage/{book_title}/{page_no}')