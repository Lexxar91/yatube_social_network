from django.urls import path
from .views import view_news
app_name = 'news'

urlpatterns = (
    path('news_page', view_news, name='view_news'),
)
