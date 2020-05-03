from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage, AccessRecord, Topic
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    content = {'access_rec': webpages_list}
    return render(request, 'first_app/base.html', context=content)


def help(request):
    content = {'insert_me': 'Help page'}
    return render(request, 'first_app/base.html', context=content)
