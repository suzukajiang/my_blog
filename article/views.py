from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def show_article(request):
    response = ""
    list_blog = Article.objects.all()
    for blog in list_blog:
        response += blog.title + blog.category + blog.content + " "
    return HttpResponse(response)
