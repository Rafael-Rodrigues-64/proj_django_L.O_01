from django.shortcuts import render


def home(request):
    return render(request, 'receitas_LO/home.html', context={'name': 'Rafael Rodrigues'})
