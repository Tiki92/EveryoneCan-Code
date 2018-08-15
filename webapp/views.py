from django.shortcuts import render
from django.http import HttpResponse
from .forms import CodeForm

# Create your views here.
def index(request):
    return render(request, 'webapp/home.html')

def post_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit= False)
            post_item.save()
    else:
        form = CodeForm()
    return render(request, 'webapp/post_code.html', {'form': form})

def post(request):
    return render(request, 'webapp/post_code.html')

