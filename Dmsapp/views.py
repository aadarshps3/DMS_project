import datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from Dmsapp.forms import NotificationForm, StudentForm , internal_form
from Dmsapp.models import Notification, Login, Attendance,internal_mark


# Create your views here.
def student_register(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            messages.info(request, 'student Registered Successful')
            return redirect('')
    return render(request,'student_register.html',{'form':form})

def admin_home(request):
    return render(request, 'admintemp/index.html')

def student_view(request):
    data = Login.objects.filter(is_student=True)
    return render(request,'admintemp/student_view.html',{'data':data})


def Notification_add(request):
    form = NotificationForm()
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Notification_view')
    return render(request, 'admintemp/Notification_add.html', {'form': form})

def Notification_view(request):
    data = Notification.objects.all()
    return render(request,'admintemp/Notification_view.html',{'data':data})

def add_attendance(request):
    data = Login.objects.filter(is_student=True)
    print(data)
    return render(request, 'admintemp/add_attendence.html', {'data': data})

now = datetime.datetime.now()

def mark(request, id):
    user = Login.objects.get(id=id)
    att = Attendance.objects.filter(student=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's Attendance Already marked for this Student ")
        return redirect('add_attendance')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user, date=datetime.date.today(), attendance=attndc,time=now.time()).save()
            messages.info(request, "Attendance Added successfully ")
            return redirect('add_attendance')
    return render(request, 'admintemp/mark_attendance.html')

def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendance = {}
    for value in value_list:
        attendance[value] = Attendance.objects.filter(date=value)
    return render(request, 'admintemp/view_attendance.html', {'attendances': attendance})

def add_internal_mark(request):
    form=internal_form()
    if request.method == 'POST':
        form=internal_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_internal_mark')
    return render(request,'admintemp/add_internal.html',{'form':form})

def view_internal_mark(request):
    data = internal_mark.objects.all()
    return render(request,'admintemp/view_internal.html',{'data':data})

def update_internal(request,id):
    data=internal_mark.objects.get(id=id)
    form=internal_form(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('view_internal_mark')
    return render(request,'admintemp/update_internal.html',{'form':form})

def del_internal(request,id):
    data=internal_mark.objects.get(id=id)
    data.delete()
    return redirect('view_internal_mark')







