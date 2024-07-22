from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', "Hello", "123"],
        'obj': {
            "car": 'BMW',
            "age": 18,
            "nobby": "Football"
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contacts(request):
    return render(request, 'main/contacts.html')