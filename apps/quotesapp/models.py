from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from bcrypt import hashpw
from django.contrib import messages
from itertools import count
import datetime

class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm, birthday):
        errors = []
        EMAIL_REGEX = (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(first_name) <= 2:
            errors.append("A first name with at least two character is required")
        if len(last_name) <= 2:
            errors.append("A last name with at least two character is required")
        if len(password) == 0:
            errors.append("Password is required")
        elif password != confirm:
            errors.append("Password and confrimation must match")
        if len(email) == 0:
            errors.append("Email is required")
        elif not re.match(EMAIL_REGEX, email):
            errors.append("Valid email is required")
        if len(errors) is not 0:
            return (False, errors)
        else:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            Users = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed, birthday = birthday)
            return True

    def login(self, email, password):
            errors = []
            if User.objects.filter(email=email):
                user = User.objects.filter(email=email)[0]
                hashed = user.password
                if bcrypt.hashpw(password.encode(), hashed.encode()) == hashed:
                    loggedin = "Successfully created new user"
                    return True
                else:
                    errors.append("Invalid password for this email")
                    return (False, errors)
            else:
                errors.append("Invalid login credentials")
                return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=45, default='null')
    last_name = models.CharField(max_length=45, default='null')
    email = models.CharField(max_length=45, default='null')
    password = models.CharField(max_length=255, default='null')
    birthday = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

class QuoteManager(models.Manager):
    def addquote(self, user, quote, author):
        quote_errors = []
        if len(quote) <= 3:
            quote_errors.append("A quote needs to have at least two characters.")
        if len(author) <= 10:
            quote_errors.append("An author's name needs to have at least ten characters.")
        if len(quote_errors) is not 0:
            return (False, quote_errors)
        else:
            if len(quote_errors) is not 0:
                quote_errors.pop()
            Quotes = Quote.objects.create(user = user, quote = quote, author = author)
            return True

class Quote(models.Model):
    user = models.ForeignKey(User)
    author = models.CharField(max_length=45, default='null')
    quote = models.CharField(max_length=500, default='null')
    created_at = models.DateTimeField(auto_now_add = True)
    objects = QuoteManager()

class FavoriteManager(models.Manager):
    def addfavorite(self, user, quote):
        Favorites = Favorite.objects.create(user = user, quote = quote)
        return (True)

class Favorite(models.Model):
    user = models.ForeignKey(User)
    quote = models.ForeignKey(Quote)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = FavoriteManager()
