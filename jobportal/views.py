from django.shortcuts import render
from .models import ISCO, JobAnalysis


# Create your views here.
def Occupation(request):
    data = ISCO.objects.all()
    return render(request, 'Occupation.html', {'Occupation':data})