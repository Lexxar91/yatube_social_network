from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

#  Конструкция class Meta(UserCreationForm.Meta)
#  описывает обычное наследование, только наследуется не основной класс, а вложенный:

#Данные, переданные из форм, на сервере проверяются функциями-валидаторами. 
# Валидатор обращается к данным (или получает их в качестве аргумента) и проверяет их значение.
#  В случае ошибки вызывается исключение ValidationError. В Django есть множество встроенных валидаторов, но можно написать и собственный.

#Валидация поля формы может быть многоэтапной. 
# Значения, полученные после валидации каждого из полей, будут доступны в словаре form.cleaned_data.
#  Ключи в этом словаре — названия полей формы.

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
