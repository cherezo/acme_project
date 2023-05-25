from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown

def birthday(request):
    print(request.GET)
    # Создаём экземпляр класса формы.
    # Весь фокус в выражении BirthdayForm(request.GET or None). 
    # Его логика такова: если в GET-запросе были переданы параметры — значит, объект request.GET не пуст 
    # и этот объект передаётся в форму; если же объект request.GET пуст — срабатывает условиe or 
    # и форма создаётся без параметров, через BirthdayForm(None) — это идентично обычному BirthdayForm()
    form = BirthdayForm(request.GET or None)
    # Добавляем его в словарь контекста под ключом form:
    context = {'form': form}
    if form.is_valid():
        # ...вызовем функцию подсчёта дней:
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})
    
    # Указываем нужный шаблон и передаём в него словарь контекста.
    return render(request, 'birthday/birthday.html', context=context)
