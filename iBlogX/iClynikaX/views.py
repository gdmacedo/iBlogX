from django.shortcuts import render
from .models import Cliente


def fnct_blog_home(request):
    clientes = Cliente.objects.all()
    return render(request, 'ecomm/index.html', {'clientes': clientes})
