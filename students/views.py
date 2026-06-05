from django.shortcuts import render
from django.http import HttpResponse

def student_list(request):
    return render(request, 'students/students_list.html')