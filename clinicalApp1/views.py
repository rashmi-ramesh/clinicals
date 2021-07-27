from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from clinicalApp1.models import Patient,ClinicalData
from clinicalApp1.forms import ClinicalDataForm

# Create your views here.
class PatientListView(ListView):
    model = Patient

class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName','lastName','age')

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName','lastName','age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

def addData(request,**kwargs):
    patient = Patient.objects.get(id=kwargs['pk'])
    form = ClinicalDataForm()
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'clinicalApp1/clinicalData_form.html',{'form':form,'patient':patient})

def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'Height/Weight':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                feetToMeter = float(heightAndWeight[0]) * 0.4536
                BMI = float(heightAndWeight[1]) / (feetToMeter * feetToMeter)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalApp1/generateReport.html',{'data':responseData})
