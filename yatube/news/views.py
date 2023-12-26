from asgiref.sync import sync_to_async
from django.core.cache import cache
from django.shortcuts import render

from .api import get_news


async def view_news(request):
    """
    Обрабатывает запрос на отображение новостей.

    Если данные новостей не кэшированы, вызывает функцию get_news(),
    сохраняет полученные данные в кэше и возвращает их.
    Если данные уже находятся в кэше, использует их для отображения.

    Аргументы:
       - request: запрос от пользователя

    Возвращает страницу с новостями в формате HTML.
    """
    cached_news = cache.get('news_page')
    if cached_news is None:
        news_data = await get_news()
        cache.set('news_page', news_data, timeout=300)
    else:
        news_data = cached_news
    context = {
        'news': news_data
    }

    return await sync_to_async(render)(request, 'news/news.html', context)
