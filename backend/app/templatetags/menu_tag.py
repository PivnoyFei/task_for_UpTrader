from typing import Any

from app.models import Menu
from django import template
from django.core.paginator import Page, Paginator
from menu.settings import PAGE_SIZE

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: Any, main_menu: str | None = None) -> Page:
    if main_menu:
        obj = Menu.objects.filter(slug=main_menu).prefetch_related('children')
    else:
        obj = Menu.objects.filter(parent=None).prefetch_related('children')

    paginator = Paginator(obj, PAGE_SIZE)
    page = context['request'].GET.get('page', 1)
    return paginator.page(page)
