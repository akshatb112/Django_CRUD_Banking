from django.shortcuts import render, redirect  
from Branch.forms import BranchForm  
from Branch.models import Branch


def branc(request):  
    if request.method == "POST":  
        form = BranchForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/branch_show')  
            except:  
                pass  
    else:  
        form = BranchForm()  
    return render(request,'index.html',{'form':form})  
def branch_show(request):  
    branches = Branch.objects.all().order_by('id')  
    return render(request,"branch_show.html",{'branches':branches})  
def edit(request, id):  
    branch = Branch.objects.get(id=id)  
    return render(request,'edit.html', {'branch':branch})  
def update(request, id):  
    branch = Branch.objects.get(id=id)  
    form = BranchForm(request.POST, instance = branch)  
    if form.is_valid():  
        form.save()  
        return redirect("/branch_show")  
    return render(request, 'edit.html', {'branch': branch})  
def destroy(request, id):  
    branch = Branch.objects.get(id=id)  
    branch.delete()  
    return redirect("/branch_show")  