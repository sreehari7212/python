from django.shortcuts import render, redirect

# Create your views here.
from aa_app.forms import StudentForm
from aa_app.models import Student


def home(request):
    return render(request,'home.html')


def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_register')
    return render(request, 'student_add.html', {'form': form})

def student_view(request):
    stud = Student.objects.all()
    return render(request,'student_view.html',{'stud':stud})
