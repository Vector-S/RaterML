from django.shortcuts import render
from django.http import HttpRequest
from health_manager.models import Weight
from health_manager.forms import NewWeightForm

# Create your views here.
def health(request):
    form = NewWeightForm()
    if request.method=="POST":
        form = NewWeightForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("INVALID FORM")
    weights = Weight.objects.order_by('datetime')
    context = {'weights':weights,
               'form':form}
    return render(request,'health_manager/health.html',context)
