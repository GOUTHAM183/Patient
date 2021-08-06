from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Patient
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    CreateView,
    DetailView,
)
from django.urls import reverse_lazy,reverse


# Create your views here.
def home(request):
    context = {"patients": Patient.objects.all()}
    return render(request, "PD/home.html", context)

class PatientListView(ListView):
    model = Patient
    template_name = "PD/home.html"
    context_object_name = "patients"

class PatientDetailView(DetailView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    fields = ["firstname","lastname","gender","age","disease","doctor","fees","medsstarted"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PatientUpdateView( UpdateView):
    model = Patient
    fields = ["firstname","lastname","gender","age","disease","doctor","fees","medsstarted"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        patients = Patient.objects.filter(firstname__contains=searched)
        

        return render(request,'PD/search.html',{'searched':searched,'patients':patients})
    else:
        return render(request,'PD/search.html',{})  


class PatientDeleteView( DeleteView):
    model = Patient
    success_url = "/"

    