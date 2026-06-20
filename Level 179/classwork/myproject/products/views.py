from django.shortcuts import render
from django.http import HttpResponse

products_database = [
    {'id': 0, 'title': 'ზანგის ღიმილი', 'price': 5.99},
    {'id': 1, 'title': 'ვაშლი', 'price': 1.50},
    {'id': 2, 'title': 'ბანანი', 'price': 2.20},
    {'id': 3, 'title': 'ატამი', 'price': 3.10},
    {'id': 4, 'title': 'მსხალი', 'price': 2.80},
    {'id': 5, 'title': 'მარწყვი', 'price': 4.50},
    {'id': 6, 'title': 'კივი', 'price': 2.40},
    {'id': 7, 'title': 'ანანასი', 'price': 6.99},
    {'id': 8, 'title': 'ყურძენი', 'price': 3.75},
    {'id': 9, 'title': 'საზამთრო', 'price': 7.20},
]

def product_info(request, id):
    context = list(filter(lambda a:a['id'] == id, products_database))[0] 
    print(context)
    return render(request, 'products_details.html', context)