from django.shortcuts import render

# Create your views here.
students_database = [
    {"id": 0, "name": "ნიკა", "age": 15, "grade": 9},
    {"id": 1, "name": "მარიამი", "age": 14, "grade": 8},
    {"id": 2, "name": "გიორგი", "age": 16, "grade": 10},
    {"id": 3, "name": "ანი", "age": 17, "grade": 11},
    {"id": 4, "name": "ლუკა", "age": 15, "grade": 9},
    {"id": 5, "name": "ელენე", "age": 18, "grade": 12},
    {"id": 6, "name": "დავითი", "age": 14, "grade": 8},
    {"id": 7, "name": "ნინო", "age": 16, "grade": 10},
    {"id": 8, "name": "სანდრო", "age": 15, "grade": 9},
    {"id": 9, "name": "თამარი", "age": 17, "grade": 11},
    {"id": 10, "name": "ირაკლი", "age": 14, "grade": 8},
    {"id": 11, "name": "სალომე", "age": 16, "grade": 10},
    {"id": 12, "name": "ლაშა", "age": 18, "grade": 12},
    {"id": 13, "name": "ქეთევან", "age": 15, "grade": 9},
    {"id": 14, "name": "ზურა", "age": 17, "grade": 11},
    {"id": 15, "name": "ლიზა", "age": 14, "grade": 8},
    {"id": 16, "name": "ბექა", "age": 16, "grade": 10},
    {"id": 17, "name": "თეონა", "age": 15, "grade": 9},
    {"id": 18, "name": "საბა", "age": 18, "grade": 12},
    {"id": 19, "name": "ალექსანდრე", "age": 17, "grade": 11},
    {"id": 20, "name": "ნატა", "age": 14, "grade": 8},
    {"id": 21, "name": "ოთარი", "age": 16, "grade": 10},
    {"id": 22, "name": "მარი", "age": 15, "grade": 9},
    {"id": 23, "name": "ლევანი", "age": 18, "grade": 12},
    {"id": 24, "name": "ეკა", "age": 17, "grade": 11},
    {"id": 25, "name": "გიგა", "age": 14, "grade": 8},
    {"id": 26, "name": "სოფო", "age": 16, "grade": 10},
    {"id": 27, "name": "თორნიკე", "age": 15, "grade": 9},
    {"id": 28, "name": "ანა", "age": 18, "grade": 12},
    {"id": 29, "name": "ვაჟა", "age": 17, "grade": 11}
]

def all_users(request):
    return render(request, 'students/all_users.html', {'students': students_database})

def all_info(request):
    selected_student = None

    for student in students_database:
        if student['id'] == student_id:
            selected_student = student
            break

    return render(request, 'students/all_info.html', {'student': selected_student})