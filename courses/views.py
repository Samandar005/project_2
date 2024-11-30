from django.shortcuts import render
from .models import Course

def courses_list(request):
    title = request.GET.get('title')
    descriotion = request.GET.get('descriotion')
    start_data = request.GET.get('start_data')
    end_data = request.GET.get('end_data')
    max_students = request.GET.get('max_students')
    if (title and
            descriotion and
            start_data and
            end_data and
            max_students):
        Course.objects.create(
            title=title,
            descriotion=descriotion,
            start_data=start_data,
            end_data=end_data,
            max_students = max_students
        )
    courses = Course.objects.all()
    ctx = {'courses': courses}
    return render(request, 'courses/courses-list.html', ctx)
