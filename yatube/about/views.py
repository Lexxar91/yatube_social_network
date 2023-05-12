from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    """
    Класс представления (view), который отображает шаблон 'about/author.html'.
    """
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    """
    Класс представления (view), который отображает шаблон 'about/tech.html'.
    """
    template_name = 'about/tech.html'
