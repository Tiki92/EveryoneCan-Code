from django.shortcuts import render
from add_code.forms import CodeForm
from django.contrib import messages



# Create your views here.
def post_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit= False)
            post_item.save()
            form= CodeForm()
            messages.success(request, 'Code has been added to the database!, Thank you form your contribution.')
    else:
        form = CodeForm()
    return render(request, 'webapp/post_code.html', {'form': form})


