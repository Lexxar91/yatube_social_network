from typing import Optional, List, Dict, Any, Tuple

import aiohttp
from .errors_api import ERROR_CODES
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_news() -> Optional[List[Dict[str, Any]]]:
    """
    Получает данные новостей из News API.

    Возвращает список словарей, содержащих информацию о новостных статьях.
    Каждый словарь содержит следующие ключи:
    - 'author': Автор статьи (если доступно)
    - 'title': Заголовок статьи
    - 'description': Описание ста
    - 'url': Ссылка URL на статью
    - 'publishedAt': Время публикации статьи

    Возвращает None, если происходит ошибка во время запроса.
    """
    api_key = os.getenv('NEWS_API_KEY')
    api_url = f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={api_key}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                data: Dict[str, Any] = await response.json()
                if response.status != 200:
                    error_code = data.get('code')
                    error_message = data.get('message')
                    if error_code in ERROR_CODES:
                        logger.error(ERROR_CODES[error_code])
                    else:
                        logger.error(f"Произошла ошибка: {error_message}")
                    return None
                articles = data['articles']
                keys: Tuple[str, str, str, str, str] = ("author", "title", "description", "url", "publishedAt",)
                return [{key: article.get(key, None) for key in keys} for article in articles]
    except aiohttp.ClientError as e:
        logger.error(f"Произошла ошибка во время запроса: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Произошла другая ошибка: {str(e)}")
        return None
