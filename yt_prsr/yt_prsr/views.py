from django.shortcuts import render


def index(request):
    return render(request, 'yt_prsr/index.html')