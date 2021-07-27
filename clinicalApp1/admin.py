from django.contrib import admin
from clinicalApp1.models import Patient,ClinicalData

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['firstName','lastName']

admin.site.register(Patient,PatientAdmin)
admin.site.register(ClinicalData)