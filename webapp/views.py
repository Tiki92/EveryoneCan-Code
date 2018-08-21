from django.shortcuts import render
from add_code.models import Code
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    page_code = Code.objects.all()
    paginator = Paginator(page_code, 10)

    page = request.GET.get('page')
    list_code = paginator.get_page(page)
    return render(request, 'webapp/home.html', {'list_code': list_code})


def detailed(request, code_id):
    detail = Code.objects.all()
    post = Code.objects.get(id=code_id)
    return render(request, 'webapp/detailed_view.html', {'detail': detail, 'post': post})




