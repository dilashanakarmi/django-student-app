from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Student

def home(request):
    return render(request, 'students/home.html')

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    return render(request, 'students/contact.html')

def students_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'total_students': students.count(),
    }
    return render(request, 'students/students_list.html', context)

def students_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'students/students_detail.html', context)

# Custom 404 Error Handler
def page_not_found(request, exception):
    return render(request, '404.html', status=404)