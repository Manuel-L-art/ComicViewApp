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

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False
        user = users[0]
        return bcrypt.checkpw(password.encode(),user.password.encode())
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
    release_date = models.DateTimeField()

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comicpage = models.ForeignKey(Comic,related_name="comicPage", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    reply = models.TextField()
    user = models.ManyToManyField(Comment, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



