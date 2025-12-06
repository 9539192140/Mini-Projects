from django.shortcuts import render,redirect,get_object_or_404
from .models import datas  
# Create your views here.
def home (request):
    sort_order = request.GET.get('sort', 'desc')  # Default is descending
    if request.method=="POST": 
       title=request.POST.get("head")  
       content=request.POST.get("note")
       print(title)
       print(content)
       datas.objects.create(
           head=title,
           note=content
       )
    data = datas.objects.all().order_by('-id') 
    for i in data: 
           print(i.head)
           print(i.note)
    if sort_order == 'asc':
        data = datas.objects.all().order_by('id')  # Oldest first
    else:
        data = datas.objects.all().order_by('-id')  # Newest first
    return render(request,"home.html",{"data":data})
def delete(request,pk):
     obj=get_object_or_404(datas,pk=pk)
     obj.delete()
     return redirect("home")
def update(request,pk):
    order=get_object_or_404(datas,pk=pk)
    if request.POST:
         order.head=request.POST.get('head')
         order.note=request.POST.get('note')
         order.save()
         return redirect('home')
    context={
         "data":order 
    } 

    return render(request,"update.html",context)