from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist

from .models import Product

def index(request):
    return HttpResponse('Hello World')

def page(request, page_num):
    return HttpResponse(f'Page {page_num}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        # return HttpResponseNotFound('NOT FOUND')
        raise Http404('NOT FOUND')

    return HttpResponse('OK!')





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