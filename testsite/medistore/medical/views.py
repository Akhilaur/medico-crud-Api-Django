from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import medicalmedicines
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import date 

from datetime import datetime


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/") 
        else:
            messages.info(request, 'invalid user')
            return render(request, 'login.html') 

    else:
        return render(request, 'login.html')


def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']    
        last_name = request.POST['last_name'] 
        username = request.POST['username'] 
        email = request.POST['email'] 
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already exist..")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"Email is already exists..")
                 return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
             messages.info(request,"password is not matched...........")
             return redirect('register')
        
    
    
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('index')



@login_required(login_url='login')
def addrecord(request):
    return render(request, 'addrecord.html')
                                                                                                    
     
def add(request):
    name = request.POST['medicine_name']
    cmp = request.POST['company_name']
    date = request.POST['date']
    amount = request.POST['amount']
    
    
    medical_medicines = medicalmedicines(
        medicine_name=name, company_name=cmp, date=date, amount=amount)
    medical_medicines.save()

    return render(request, 'addrecord.html')


@login_required(login_url='login')
def medicinelist(request):
 medicine = medicalmedicines.objects.all()
 context = {
     'medicine': medicine
    }

 return render(request, 'list.html', context)      




def delete(request, id):  
    dele = medicalmedicines.objects.get(id=id) 
    dele.delete()
    print("sucessfully deleted!")
    return redirect(medicinelist)



@login_required(login_url='login')
def edit(request, id):
    upd = medicalmedicines.objects.get(id=id)
    
    return render(request, 'edit.html', {'upd': upd})

@login_required(login_url='login')
def updaterecord(request, id):
    name = request.POST['medicine_name']
    cmp = request.POST['company_name']
    
    amount = request.POST['amount']                      

    upd = medicalmedicines.objects.get(id=id)
    upd.medicine_name = name
    upd.company_name = cmp 
    upd.amount = amount
    upd.save()
    print(upd)
    return redirect(medicinelist)         


def search(request):
    sear = request.GET['sear']
    medicine = medicalmedicines.objects.filter(medicine_name__istartswith=sear)
   

    param = {'medicine': medicine}
    return render(request, 'search.html', param)                                   


def index(request):
    return render(request, 'index.html')

def home(request):
 
 now=datetime.now()
 context = {
         'now': now
    }
 return render(request ,'home.html',context) 



















