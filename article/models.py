# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    pub_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True, null=True)
    content = models.TextField(blank = True, null = True)

    def __unicode__(self) :
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'article'
        verbose_name_plural = 'article'
