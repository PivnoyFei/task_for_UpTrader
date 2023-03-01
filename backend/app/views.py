from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class MenuView(View):
    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        slug = kwargs.get('slug', None)
        context = {'menu_name': slug, 'title': slug if slug else 'Главная'}
        return render(request, 'index.html', context)
