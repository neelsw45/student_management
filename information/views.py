from django.shortcuts import render,redirect
from .models import Addmission,Contact

# Create your views here.

def home(request):
    query=request.GET.get('q','')

    if query:
        stu_detail=Addmission.objects.filter(sname__icontains=query)
    else:
        stu_detail=Addmission.objects.all()
    context={
        'studetail':stu_detail
    }

    return render(request,'home.html',context)

def add_student(request):
    if request.method == 'POST':
        # print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phno')
        enrollno=request.POST.get('enno')
        addate=request.POST.get('addate')
        fees = True if request.POST.get('fees') == 'Yes' else False
        Addmission.objects.create(
            sname=name,
            semail=email,
            sphoneno=phoneno,
            senrollno=enrollno,
            sadddate=addate,
            paid_fees = fees
        )
        return redirect('home')

    return render(request,'add_student.html')

def student_details(request):
    stu_detail=Addmission.objects.all()
    context={
        'studetail':stu_detail,
    }
    return render(request,'stu_detail.html',context)


def spe_detail(request,pk):
    stu_detail=Addmission.objects.get(id=pk)
    context={
        'studetail':stu_detail
    }
    return render(request,'spe_detail.html',context)

def edit_student(request,pk):
    stu_detail=Addmission.objects.get(id=pk)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phno')
        enrollno=request.POST.get('enno')
        adddate=request.POST.get('addate')
        stu_detail.sname=name
        stu_detail.semail=email
        stu_detail.sphoneno=phoneno
        stu_detail.senrollno=enrollno
        stu_detail.sadddate=adddate
        stu_detail.save()
        return redirect('student_detail')
    # if stu_detail.sadddate:
    #     stu_detail.sadddate = stu_detail.sadddate.strftime('%Y-%m-%d')
    context={
        'studetail':stu_detail
    }
    
    return render(request,'edit_student.html',context)

def delete_student(request,pk):
    stu_detail=Addmission.objects.get(id=pk)
    if request.method=='POST':
        stu_detail.delete()
        return redirect('home')
    
    context={
        'studetail':stu_detail
    }

    return render(request,'delete_action.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        desc=request.POST.get('desc')
        Contact.objects.create(
            name=name,
            email=email,
            phno=phno,
            desc=desc,
        )
        return redirect('contact_action')
    
    return render(request,'contact.html')

def contact_action(request):
    return render(request,'action_contact.html')