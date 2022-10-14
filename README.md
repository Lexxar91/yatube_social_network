## Yatube-_social_network

### Описание:

Социальная сеть блогеров. _Учебный проект_.
Сообщество для публикаций. Блог с возможностью публикации постов, подпиской на авторов, а также комментированием постов.

### Стэк технологий:

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Pillow](https://img.shields.io/badge/-Pillow-464646?style=flat-square&logo=Pillow)](https://pypi.org/project/Pillow/)
[![Thumbnail](https://img.shields.io/badge/-Thumbnail-464646?style=flat-square&logo=Thumbnail)](https://pypi.org/project/thumbnail/)

### Запуск проекта в dev-режиме:

Инструкция ориентирована на операционную систему windows и утилиту git bash.
Для прочих инструментов используйте аналоги команд для вашего окружения.

1.Клонируйте репозиторий и перейдите в него в командной строке:

```git clone https://https://github.com/Lexxar91/yatube_social_network```
```cd yatube_social_network```

2.Установите и активируйте виртуальное окружение:
```python -m venv venv```
```source venv/Scripts/activate```

3.Установите зависимости из файла requirements.txt:
```pip install -r requirements.txt```

4.В папке с файлом manage.py выполните миграции:
```python manage.py migrate```

5.В папке с файлом manage.py запустите сервер, выполнив команду:
```python manage.py runserver```

### Что могут делать пользователи:

Залогиненные пользователи могут:

1.Просматривать, публиковать, свои публикации;<br>
2.Просматривать информацию о сообществах;<br>
3.Просматривать и публиковать комментарии от своего имени к публикациям других пользователей (включая самого себя);<br>
4.Подписываться на других пользователей и просматривать свои подписки.<br>

### Анонимные 👽 пользователи могут:

1.Просматривать публикации;<br>
2.Просматривать информацию о сообществах;<br>
3.Просматривать комментарии;<br>

### UPD:
Добавлена авторизация на сайте через соц.сеть Вконтакте через протокол Oauth 2.0
Для добавления данного функционала использовалась библиотека Django-allauth.
