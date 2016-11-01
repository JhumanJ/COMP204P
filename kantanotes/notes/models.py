from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    """Category"""
    categoryName = models.CharField('category', max_length=255)
    description = models.TextField('description', blank=True)
    userId = models.ForeignKey(User)

    def __str__(self):
        return self.description



class Notes(models.Model):
    """Note"""
    title = models.CharField('title', max_length=255)
    description = models.CharField('description', max_length=255, blank=True)
    userId = models.ForeignKey(User)
    categoryId = models.ForeignKey(Categories, verbose_name='category', related_name='notes')
    # TODO:  implements validator

    def __str__(self):
        return self.title


class Links(models.Model):
    """Note"""
    url = models.CharField('Note Url', max_length=255, blank=True)
    noteId = models.ForeignKey(Notes, verbose_name='note', related_name='links')

    def __str__(self):
        return self.url


