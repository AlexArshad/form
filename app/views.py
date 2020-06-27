from django.shortcuts import render, get_object_or_404, redirect
from app.forms import StudentForm
from app.models import Student

# Create your views here.

def data_views(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()

    return render(request,'index.html',{'form':form})

def show_views(request):

    students = Student.objects.all()

    return render(request,"show.html",{'students':students})

def edit_views(request, id):

    students = Student.objects.filter(id=id)

    return render(request,'edit.html', {'students':students})

def update_views(request, id):

    students = Student.objects.filter(id=id)
    form = StudentForm(request.POST or None, instance = students)

    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html', {'students': students})

def delete_views(request, id):

    students = Student.objects.get(id=id)
    students.delete()

    return redirect("/show")