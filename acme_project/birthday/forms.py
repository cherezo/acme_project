from django import forms
# Импортируем класс модели Birthday.
from .models import Birthday, Congratulation
# Импортируем класс ошибки валидации.
from django.core.exceptions import ValidationError
# Импорт функции для отправки почты.
from django.core.mail import send_mail


# Множество с именами участников Ливерпульской четвёрки.
BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}

#Создание формы на основе модели
class BirthdayForm(forms.ModelForm):

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        # fields = '__all__'
        # Указываем, что надо отобразить все поля за исключением поля author.
        exclude = ('author',)
        #Не забываем указание требуемых виджетов (например для поля 'birthday')
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        # Получаем значение имени из словаря очищенных данных.
        first_name = self.cleaned_data['first_name']
        # Разбиваем полученную строку по пробелам 
        # и возвращаем только первое имя.
        return first_name.split()[0]

    def clean(self):
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            # Отправляем письмо, если кто-то представляется 
            # именем одного из участников Beatles.
            send_mail(
                subject='Another Beatles member',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            ) 

class CongratulationForm(forms.ModelForm):
    
    class Meta:
        model = Congratulation
        fields = ('text',)

#Создание самостоятельной формы
'''
class BirthdayForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        max_length=20
    )
    last_name = forms.CharField(
        label='Фамилия',
        required=False,
        help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'})    
    )
'''