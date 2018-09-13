from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.utils.text import Truncator
from markdown import markdown
# Create your models here.

class Accounts(models.Model):
    gender_choices = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, validators=[MinValueValidator(1)])
    name = models.CharField(max_length=20 , null=True)
    gender = models.CharField(max_length=10 , choices=gender_choices, default='male')
    def __unicode__(self):
        return self.age


class Books(models.Model):
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=15,  null=True)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.book_name


class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')


    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)



class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title