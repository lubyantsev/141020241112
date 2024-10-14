from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/home.html')


def shop(request):
    items = {
        'item1': 'Игровая консоль',
        'item2': 'Игра A',
        'item3': 'Игра B',
    }
    return render(request, 'fourth_task/shop.html', context={'items': items})


def cart(request):
    return render(request, 'fourth_task/cart.html')
