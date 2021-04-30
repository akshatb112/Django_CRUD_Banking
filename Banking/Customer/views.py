from django.shortcuts import render, redirect  
from Customer.forms import CustomerForm  
from Customer.models import Customer


def cus(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    branches = Customer.objects.all()  
    return render(request,"show.html",{'branches':branches})  
def edit(request, id):  
    branch = Customer.objects.get(id=id)  
    return render(request,'edit.html', {'branch':branch})  
def update(request, id):  
    branch = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST, instance = branch)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'branch': branch})  
def destroy(request, id):  
    branch = Customer.objects.get(id=id)  
    branch.delete()  
    return redirect("/show")  