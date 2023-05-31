from django.db import models
# Импортируется функция-валидатор.
from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)


'''Добавим к модели Birthday проверку на уникальность записи: совокупность значений полей
 «Имя», «Фамилия» и «Дата рождения» не должна повторяться в БД. 
Подобные проверки настраиваются с помощью атрибута constraints (англ. «ограничения») подкласса Meta,
 где указывается класс model.UniqueConstraint (ограничение на уникальность). 
В этом классе указывается:
- перечень полей, совокупность которых должна быть уникальна;
- имя ограничения.
'''
class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
