from django.shortcuts import render

cars_database = [
    {'id': 0, 'title': 'Toyota Camry', 'price': 25000},
    {'id': 1, 'title': 'Honda Civic', 'price': 22000},
    {'id': 2, 'title': 'BMW X5', 'price': 65000},
    {'id': 3, 'title': 'Mercedes-Benz C-Class', 'price': 55000},
    {'id': 4, 'title': 'Audi A4', 'price': 48000},
    {'id': 5, 'title': 'Volkswagen Golf', 'price': 28000},
    {'id': 6, 'title': 'Ford Mustang', 'price': 45000},
    {'id': 7, 'title': 'Chevrolet Camaro', 'price': 43000},
    {'id': 8, 'title': 'Nissan Altima', 'price': 26000},
    {'id': 9, 'title': 'Hyundai Elantra', 'price': 23000},
    {'id': 10, 'title': 'Kia Sportage', 'price': 29000},
    {'id': 11, 'title': 'Mazda CX-5', 'price': 31000},
    {'id': 12, 'title': 'Subaru Outback', 'price': 34000},
    {'id': 13, 'title': 'Lexus RX', 'price': 58000},
    {'id': 14, 'title': 'Tesla Model 3', 'price': 42000},
    {'id': 15, 'title': 'Tesla Model Y', 'price': 50000},
    {'id': 16, 'title': 'Jeep Wrangler', 'price': 41000},
    {'id': 17, 'title': 'Land Rover Defender', 'price': 75000},
    {'id': 18, 'title': 'Porsche Cayenne', 'price': 85000},
    {'id': 19, 'title': 'Volvo XC90', 'price': 67000},
    {'id': 20, 'title': 'Jaguar F-Pace', 'price': 62000},
    {'id': 21, 'title': 'Ferrari Roma', 'price': 250000},
    {'id': 22, 'title': 'Lamborghini Huracan', 'price': 280000},
    {'id': 23, 'title': 'McLaren 720S', 'price': 300000},
    {'id': 24, 'title': 'Bugatti Chiron', 'price': 3000000},
    {'id': 25, 'title': 'Rolls-Royce Phantom', 'price': 460000},
    {'id': 26, 'title': 'Bentley Continental GT', 'price': 240000},
    {'id': 27, 'title': 'Aston Martin DB11', 'price': 220000},
    {'id': 28, 'title': 'Maserati Ghibli', 'price': 90000},
    {'id': 29, 'title': 'Alfa Romeo Giulia', 'price': 52000},
]

# Create your views here.
def all_cars(request):
    context = {'cars': cars_database}   
    return render(request, 'all_cars.html', context)


def car_info(request, title):
    context = list(filter(lambda a:a['title'] == title, cars_database))[0]
    
    return render(request, 'car_info.html', context)