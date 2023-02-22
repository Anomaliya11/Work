from django.shortcuts import render

def main(request):
    return render(request, 'web_lib/main.html')
