from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


# Create your views here.
from .forms import StudentForm
from .models import Student


#showing student list

def index(request):
    students = Student.objects.all() #fetch all students from database
    return render(request, 'students/index.html', {'students':students})

#adding student details
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'students/add_students.html', {'form':form})

#edit student details
def edit_student(request, id):
    student = get_object_or_404(Student, id=id) 

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)  

    return render(request, 'students/edit_student.html', {'form':form})

#delete student details
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
    return redirect('student_list')
