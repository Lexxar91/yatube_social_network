from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordChangeView, PasswordResetDoneView
from django.urls import path
from . import views

app_name = 'users'
#  Задача приложения users — расширить и изменить работу встроенного приложения django.contrib.auth.
#  Для этого, в первую очередь, нужно перенаправить все запросы, начинающиеся с /auth , в новое приложение.
#  Важно, чтобы в головном списке urlpatterns пути приложения users были размещены выше, чем пути приложения django.contrib.auth.

# Импортируем из приложения django.contrib.auth нужный view-класс

urlpatterns = (
    ## Прямо в описании обработчика укажем шаблон, 
      # который должен применяться для отображения возвращаемой страницы.
      # Да, во view-классах так можно! Как их не полюбить.
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path(
      'password_reset/',
       PasswordResetView.as_view(template_name='users/password_reset_form.html'),
       name='password_reset'),
    path(
      'password_change/', 
      PasswordChangeView.as_view(template_name='users/password_change_form.html'),
      name='password_change'),
    path(
      'password_reset/done/',
      PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
      name='password_reset_done'
    )
)