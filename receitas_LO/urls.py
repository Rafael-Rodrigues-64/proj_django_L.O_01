from django.urls import path
from receitas_LO.views import home


urlpatterns = [
    path('', home),
]
