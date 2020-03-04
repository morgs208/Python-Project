from __future__ import unicode_literals
from django.db import models
from login_app.models import User
from django.contrib import messages
import re
TIME_REGEX = re.compile(r'^[0-9]')


class MCManager(models.Manager):
    def comment_validator(self, postData):
        errors = {}
        if not TIME_REGEX.match(postData["duration_sec"]):
            errors["duration_sec"] = "Numbers only"
        if not TIME_REGEX.match(postData["duration_min"]):
            errors["duration_min"] = "Numbers only"
        if len(postData["title"]) < 1:
            errors["title"] = "Title needs to be there, sorry"
        return errors
    def c_validation(self, postData):
        errors = {}
        if len(postData["comment"]) < 2:
            errors["comment"] = "Comment needs to be longer, sorry"
        return errors
        
class Moment(models.Model):
    title = models.CharField(max_length=25)
    duration_min = models.IntegerField(null=True)
    duration_sec = models.IntegerField(null=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="user_moments", on_delete=models.CASCADE)
    objects = MCManager()

class Comment(models.Model):
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    moment = models.ForeignKey(Moment, related_name="moment_comments", on_delete=models.CASCADE)
    objects = MCManager()


