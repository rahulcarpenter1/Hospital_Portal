from django.shortcuts import render, redirect
from main.forms import CrudForm
from main.models import Crud

def home(request):
    patient = Crud.objects.all().order_by('-id')
    total = Crud.objects.all().count()
    admit = Crud.objects.filter(status="Admit").count()
    discharge = Crud.objects.filter(status="Discharge").count()
    return render(request, "index.html", {"patient":patient, "total":total,"admit":admit,"discharge":discharge})

def delete(request, id):
    patient = Crud.objects.get(id=id)
    patient.delete()
    return redirect("home")

def update(request, id):
    name = ""
    up = Crud.objects.get(id = id)
    if request.method == "POST":
        form = CrudForm(request.POST, instance=up)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            name = "your form is invalid"
    else:
        data = CrudForm(instance=up)
    return render(request, "update.html", {'crud':data, "name":name})

def forms(request):
    name = ""
    patient = Crud.objects.all()
    data = CrudForm()
    if request.method == "POST":
        form = CrudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            name = "your form is invalid"
    return render(request, "form.html", {'crud':data, "name":name, "patient":patient})

def search(request):
    query = request.GET.get("q")
    patient = Crud.objects.filter(name__icontains=query)
    
    return render(request, "search.html", {"patient":patient,"query":query})