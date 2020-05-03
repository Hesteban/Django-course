from django.shortcuts import render
from . import forms


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES=['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'registration.html', {'user_form': user_form,
                                                 'profile_form': profile_form,
                                                 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                print("logged")
                print(user.is_authenticated)
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('User not active')

        else:
            print('User not registered: {}, {}'.format(username, password))
            return HttpResponse('Invalid credentials')

    else:
        print("HERE!!")
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))
