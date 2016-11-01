from __future__ import unicode_literals
from django.db import models

class Notes(models.Model):
    """Note"""
    title = models.CharField('title', max_length=255)
    url = models.CharField('Note Url', max_length=255, blank=True)
    description = models.CharField('description', max_length=255, blank=True)
    userId = models.ForeignKey(Users, verbose_name='user', related_name='notes')
    categoryId = models.ForeignKey(Categories, verbose_name='category', related_name='notes')
    # TODO:  implements validator

    def __str__(self):
        return self.name


class Categories(models.Model):
    """Category"""
    categoryName = models.CharField('category', max_length=255)
    description = models.TextField('description', blank=True)
    userId = models.ForeignKey(User, verbose_name='user', related_name='impressions')

    def __str__(self):
        return self.comment
        


