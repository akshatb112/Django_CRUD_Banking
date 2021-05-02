from django.shortcuts import render, redirect  
from BankAccount.forms import BankAccountForm  
from BankAccount.models import BankAccount
from Customer.models import Customer
from Branch.models import Branch 


def acc(request):
    customers = Customer.objects.all().order_by('id')
    branches = Branch.objects.all().order_by('id')      
    if request.method == "POST":  
        form = BankAccountForm(request.POST)  
        print(form.errors)
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/account_show')  
            except:  
                pass  
    else:  
        form = BankAccountForm()  
    return render(request,'acc_index.html',{'form':form, 'customers':customers, 'branches':branches})  
def account_show(request):  
    accounts = BankAccount.objects.all().order_by('id')  
    return render(request,"acc_show.html",{'accounts':accounts})  
def edit(request, id):  
    account = BankAccount.objects.get(id=id)  
    return render(request,'acc_edit.html', {'account':account})  
def update(request, id):  
    account = BankAccount.objects.get(id=id)  
    form = BankAccountForm(request.POST, instance = account)
    print(form.errors)  
    if form.is_valid():  
        form.save()  
        return redirect("/account_show")  
    return render(request, 'acc_edit.html', {'account': account})  
def destroy(request, id):  
    account = BankAccount.objects.get(id=id)  
    account.delete()  
    return redirect("/account_show")  

def customer_show(request):  
    customers = Customer.objects.all().order_by('id')  
    return render(request,"acc_index.html",{'customers':customers}) 