from django.shortcuts import render, redirect  
from Customer.forms import CustomerForm  
from Customer.models import Customer


def cus(request):  
    if request.method == "POST":  
        form = CustomerForm(request.POST,request.FILES)
        print(form.errors)  
        if form.is_valid():  
            try:  
                form.save()
                img_obj = form.instance  
                return redirect('/show',{'img_obj': img_obj})

            except:  
                pass  
    else:  
        form = CustomerForm()  
    return render(request,'cus_index.html',{'form':form})  
def show(request):  
    customers = Customer.objects.all().order_by('id')  
    return render(request,"cus_show.html",{'customers':customers})  
def edit(request, id):  
    customer = Customer.objects.get(id=id)  
    return render(request,'cus_edit.html', {'customer':customer})  
def update(request, id):  
    customer = Customer.objects.get(id=id)  
    form = CustomerForm(request.POST,request.FILES, instance = customer)
    print(form.errors)  
    if form.is_valid():  
        form.save()
        img_obj = form.instance  
        return redirect("/show",{'img_obj': img_obj})  
    return render(request, 'cus_edit.html', {'customer': customer})  
def destroy(request, id):  
    customer = Customer.objects.get(id=id)  
    customer.delete()  
    return redirect("/show")  