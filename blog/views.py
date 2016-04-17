from django.shortcuts import render


# Create your views here.
def index(request):
    data = {'mydata': "Hello World from my blog !"}
    return render(request, 'blog/index.html', data)
