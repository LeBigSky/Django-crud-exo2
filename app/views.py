from django.shortcuts import render, redirect
from .form import StudentForm
from .models import Student
# Create your views here.
def home(request):
    students= Student.objects.all()

    return render(request, 'app/home.html', {'students': students})

def create(request):
 if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
       return redirect ('error')
 else:
    form= StudentForm()

    return render(request, 'app/create_student.html', {'form': form} )

def error(request):
   return render(request, 'app/error.html')
