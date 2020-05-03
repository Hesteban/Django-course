from django.shortcuts import render
from . import forms

# Create your views here.


def index(request):
    return render(request, 'base.html')


def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data['name'])

    return render(request, 'form.html', {'form': form})
