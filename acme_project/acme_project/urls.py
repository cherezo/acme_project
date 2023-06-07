from django.contrib import admin
from django.urls import include, path,  reverse_lazy
# Импортируем настройки проекта.
from django.conf import settings
# Импортируем функцию, позволяющую серверу разработки отдавать файлы.
from django.conf.urls.static import static
# Импортируем форму создания пользователя.
from django.contrib.auth.forms import UserCreationForm
# Импортируем класс создания пользователя.
from django.views.generic.edit import CreateView

handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    # Подключаем urls.py приложения для работы с пользователями.
    path('auth/', include('django.contrib.auth.urls')),
    #Создаём адрес для регистрации пользователей и сразу отправляем в обработку
    #CBV-классу CreateView
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),

]

# Подключаем дебаг-панель:
if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов
    # из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)

# В конце добавляем к списку вызов функции static.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

