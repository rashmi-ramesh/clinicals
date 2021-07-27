from django.db import models

# Create your models here.
class Patient(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES = [('Height/Weight','Height/Weight'),('Blood Pressure','Blood Pressure'),('Heart Rate','Heart Rate')]
    componentName = models.CharField(max_length=100,choices=COMPONENT_NAMES)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)

