from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
# Create your models here.

class userManager(models.Manager):

    def validator(self, form):
        errors = {}
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = ("Invalid email address")
        email_check = self.filter(email=(form['email']))
        if email_check:
            errors['email'] = ("Email already in use")
        if len(form['pwd']) < 8:
            errors['pwd'] = ("Password must be longer than 8 characters")
        if len(form['first_name']) < 2:
            errors['first_name'] = ("First name is too short")
        if len(form['last_name']) < 2:
            errors['last_name'] = ("Last name is too short")
        return errors

    def authenticate(self, email, pwd):
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(pwd.encode(), user.pwd.encode())
    def register(self, form):
        pw = bcrypt.hashpw(form['pwd'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = form['first_name'],
            last_name = form['last_name'],
            email = form['email'],
            pwd = pw,
        )


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    pwd = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = userManager()

class Comic(models.Model):
    book_title = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    cover_art = models.FileField(upload_to="comic",null=True)
    release_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)

class ComicPage(models.Model):
    page_no = models.IntegerField()
    comicRef = models.ForeignKey(Comic, related_name="page", on_delete=models.CASCADE)
    comic_img = models.FileField(upload_to="comic")
    bookmarked = models.ManyToManyField(User, related_name="saved")
    uploaded_on = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    pageRef = models.ForeignKey(ComicPage, related_name="pcomment", on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name="liked_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    reply = models.TextField(null=True)
    user = models.ForeignKey(User, related_name="response", on_delete=models.CASCADE, null=True)
    commentRef = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


