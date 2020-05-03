from django.shortcuts import render
from second_app.models import User
from .forms import NewUser


# Create your views here.

def index(request):
    content = {'title': 'index page'}
    return render(request, 'index.html', context=content)


def users(request):
    users_list = User.objects.all()
    content = {'users_rec': users_list}
    return render(request, 'users.html', context=content)


def signup(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")

    return render(request, 'form.html', {'form': form})