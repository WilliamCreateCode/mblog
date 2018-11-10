#from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from models import Post

# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    post_lists = list()
    html = template.render(locals())
  #  for count, post in enumerate(posts):
  #      post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
  #      post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")

    return HttpResponse(html)
