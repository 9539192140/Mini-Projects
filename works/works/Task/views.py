# views.py
from django.shortcuts import render,redirect,get_object_or_404
from .models import add # Capitalized model name

def home(request): 
    if request.method == "POST": 
        work = request.POST.get("task")
        des = request.POST.get("description")
        print(work)
        print(des)
        add.objects.create(
            task=work,
            description=des
        )

    data = add.objects.all().order_by('-time')
    for i in data: 
        print(i.task)
        print(i.description)
    
    return render(request, "home.html", {"data": data})
def delete(request,pk): 
    dele=get_object_or_404(add,pk=pk)
    dele.delete()
    return redirect('home')    
def update(request,pk):
    up=get_object_or_404(add,pk=pk)
    if request.POST:
        up.task=request.POST.get('task')
        up.description=request.POST.get('description')
        up.save()
        return redirect('home')
    context={
        "data":up
    }
    return render(request,"form.html",context)