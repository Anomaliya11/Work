from django.urls import path, re_path

from service.views import index, page, about, json_show



urlpatterns = [
    path('', index, name = 'service'),
    re_path(r'^service/(?P<page_num>[0-9]{3})/$', page),
    path('about/<int:id>', about, name='about'),
    path('json', json_show, name="json_show"),
    # path('file', file_show, name="file_show"),
]

