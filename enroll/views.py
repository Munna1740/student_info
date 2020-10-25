from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User


def addAndShow(request):

    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['phone']
            ad = fm.cleaned_data['address']
            reg = User(name=nm, email=em, phone=ph, address=ad)
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stu = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'forms': fm, 'stud': stu})

def update_data(request,id):
    if request.method == 'POST':
        ud = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=ud)
        if fm.is_valid():
            fm.save()
    else:
        ud = User.objects.get(pk=id)
    fm = StudentRegistration(instance=ud)

    return render(request, 'enroll/updatestudent.html', {'forms': fm})

def delete_data(request,id):
    std = User.objects.get(pk=id)
    std.delete()
    return redirect('/')
