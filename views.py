from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def blog(request):
    return render(request, 'blog.html')

def post(request):
    return render(request, 'post.html')
