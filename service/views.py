from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.urls import reverse
from django.template.loader import get_template
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist

from .models import Product

def index(request):
    return render(request, 'index.html')
    # template = get_template('index.html')
    # return HttpResponse(template.render())

# def index(request):
    # return HttpResponse('Hello World')
    cont = {'Hello ', 'world'}
    resp = HttpResponse(cont)
    return resp

def page(request, page_num):
    return HttpResponse(f'Page {page_num}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        # return HttpResponseNotFound('NOT FOUND')
        raise Http404('NOT FOUND')

    return HttpResponse('OK!')


def json_show(req):
    data = {'cost':14, 'title':'book'}
    return JsonResponse(data)














    


# def file_show(req):
    file = 'service/images.jpeg'
    return FileResponse(open(file, 'rb'), as_attachment=True, filename='home')




    # return HttpResponse(f'{request.headers}')
    # return HttpResponse(f'{request.body}')
    # a = int(request.GET.get('a'))
    # b = int(request.GET.get('b'))
    # return HttpResponse(f'{a + b}')
    # return HttpResponse(f'{dict(request.GET)}')
    # return HttpResponse(f'{request.method}')
    # return HttpResponse(f'{request.scheme}')

    # res = HttpResponse('Hello World!')
    # # return HttpResponse(f'{res.status_code}')
    # # return HttpResponse(f'{res.content}')
    # return HttpResponseRedirect('service')
    # return HttpResponseRedirect(reverse('service'))