from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    icon = models.TextField(null=True)


class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    preview = models.CharField(max_length=50, null=True)
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        null=True
    )


class Comments(models.Model):
    content = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE
    )


class Reactions(models.Model):
    is_like = models.BooleanField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,
        null=True
    )
    comment = models.ForeignKey(
        Comments,
        on_delete=models.CASCADE,
        null=True
    )
