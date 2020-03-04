from __future__ import unicode_literals
from django.db import models
import bcrypt, re
from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        if len(postData["reg_first_name"]) < 2:
            errors["reg_first_name"] = "First Name must be at lease 3 characters"
        if len(postData["reg_last_name"]) < 2:
            errors["reg_last_name"] = "Last name must be at least 3 characters"
        if len(postData["reg_email"]) < 2:
            errors["reg_email"] = "Invalid email"
        if not EMAIL_REGEX.match(postData["reg_email"]):
            errors["reg_email"] = "Email is not a valid email"
        user = self.filter(email=postData["reg_email"])
        if user:
            errors["reg_email"] = "This email is already in use"
        if len(postData["reg_password"]) < 6:
            errors["reg_password"] = "Password must be at least 5 characters!"
        if postData["reg_password"] != postData["confirm_reg_password"]:
            errors["confirm_reg_password"] = "Passwords do not match!"
        return errors
    
    def login_validator(self, postData):
        validate = {
            "errors": {},
        }
        user = self.filter(email=postData["login_email"])
        if user:
            existing_user=user[0]
            if not bcrypt.checkpw(postData["login_password"].encode(), existing_user.password.encode()):
                validate["errors"]["login_password"] = "Password is incorrect"
            else:
                validate["user"]=existing_user
                
        else:
            validate["errors"]["login_email"] = "Email not found"
        
        return validate
  
          
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()