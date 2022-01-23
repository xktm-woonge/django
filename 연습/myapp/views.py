from http.client import HTTPResponse
from pydoc_data.topics import topics
from django.shortcuts import render, HttpResponse
import random

from matplotlib.pyplot import title


topics = [
    {'id':1, 'title':'routing', 'body' : 'Routing is ...'},
    {'id':2, 'title':'view', 'body' : 'View is ...'},
    {'id':3, 'title':'model', 'body' : 'Model is ...'},
]
# Create your views here.

def HTMLtemplate(article):
    global topics

    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f"""
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {article}
    </body>
    </html>
    
    """

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return(HTMLtemplate(article))
    
def create(request):
    return HTTPResponse('Create')

    
def read(request):
    global topics
    article = ''
    for topic in topics:
  

        if topic['id'] ==int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HTTPResponse('Read!' + id)