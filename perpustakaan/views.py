from django.shortcuts import render, redirect


def index(request):
    context = {
        'title':'Perpustakaan'
    }
    return render(request, 'index.html', context)