from django.db import models
# Импортируется функция-валидатор.
from .validators import real_age
# Импортируем функцию reverse() для получения ссылки на объект.
from django.urls import reverse


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)
    
    def get_absolute_url(self):
        # С помощью функции reverse() возвращаем URL объекта.
        return reverse('birthday:detail', kwargs={'pk': self.pk})
'''Добавим к модели Birthday проверку на уникальность записи: совокупность значений полей
 «Имя», «Фамилия» и «Дата рождения» не должна повторяться в БД. 
Подобные проверки настраиваются с помощью атрибута constraints (англ. «ограничения») подкласса Meta,
 где указывается класс model.UniqueConstraint (ограничение на уникальность). 
В этом классе указывается:
- перечень полей, совокупность которых должна быть уникальна;
- имя ограничения.
'''
class Meta:
    #Провека на уникальность записи
    constraints = (
        models.UniqueConstraint(
            fields=('first_name', 'last_name', 'birthday'),
            name='Unique person constraint',
        ),
    )
    #Если этот метод описан — CBV CreateView и UpdateView обратятся к объекту модели, 
    # получат адрес и переадресуют пользователя на него. Если же метод не описан 
    # — эти CBV будут ожидать, что адрес редиректа будет указан в атрибуте success_url.
    