from django.shortcuts import render
from .models import Student


def student_list(request):
    student_name = request.GET.get('student_name')
    ingredients = request.GET.get('ingredients')
    price = request.GET.get('price')
    type = request.GET.get('type')
    cuisine = request.GET.get('cuisine')
    if student_name is not None and ingredients is not None and price is not None and type is not None and cuisine is not None:
        Student.objects.create(
            student_name = student_name,
            ingredients = ingredients,
            price = price,
            type = type,
            cuisine = cuisine
        )
    student = Student.objects.all()
    ctx = {'students': student}
    return render(request, 'students/students-list.html', ctx)