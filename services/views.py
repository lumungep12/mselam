from django.shortcuts import render

def services(request):
    return render(request, 'services.html')

def EnvironmentalImpactAssessment(request):
    return render(request, 'EnvironmentalImpactAssessment.html')

def EnvironmentalIncidentManagement(request):
    return render(request, 'EnvironmentalIncidentManagement.html')

def EnvironmentalReporting(request):
    return render(request, 'EnvironmentalReporting.html')

def EnvironmentalImpactAssessmentTraining(request):
    return render(request, 'EnvironmentalImpactAssessmentTraining.html')
