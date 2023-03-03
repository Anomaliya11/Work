from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from web_lib.models import Author, Book, Product, Store, ExtUser

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age','email', 'info']
    change_list_template = "web_lib/button.html"
    change_form_template = "web_lib/custom_form.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('button', self.button)]
        return urls + my_urls

    def button(self, req):
        return redirect('..') # сделать шаг назад

    def info(self, obj):
        return format_html("<br>".join(obj.info()))
    info.short_description = "Информация об авторе"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        all_books = Author.objects.get(pk=object_id).book_set.all()
        extra_context['books'] = all_books
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','description','page_num']


@admin.register(ExtUser)
class ExtUserAdmin(admin.ModelAdmin):
    list_display = ['desc','is_logged']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']