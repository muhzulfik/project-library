from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    context = {
        'title':'Perpustakaan',
    }
    
    if request.method == "POST":
        username_login = request.POST.get('username', False)
        password_login = request.POST.get('password', False)

        user = authenticate(request, username=username_login, password=password_login)
        
        if user is not None:
            login(request, user)
            return redirect('pagecrud:index')

    return render(request, 'staff/index.html', context)