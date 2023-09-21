from django.views.generic import TemplateView
from django.http import HttpResponse

class MainPageView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Лазарев Константин'
        contex['email'] = 'kostik@ya.ru'
        contex['phone'] = '+79009999999'
        return contex


class AboutView(TemplateView):
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Лазарев Константин'
        contex['email'] = 'kostik@ya.ru'
        contex['phone'] = '+79009999999'
        return contex


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать!</h1>
    
        <h2>О сайте</h2>
        <p>Тут очень важный текст</p>
    
        <button onclick="document.location='/about'">Обо мне</button>

    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
            }
            
            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>Привет! Я Лазарев Константин</h1>
    </header>

    <main>
        <section>
            <h2>Опыт работы</h2>
            <ul>
                <li>Есть</li>
            </ul>
        </section>

        <section>
            <h2>Образование</h2>
            <ul>
                <li>Есть</li>
            </ul>
        </section>
    </main>

</body>
</html>
"""
    return HttpResponse(html)
