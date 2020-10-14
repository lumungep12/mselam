from django.urls import path
from . import views

urlpatterns = [
            path('services', views.services, name="services"),
            path('EIA/', views.EnvironmentalImpactAssessment, name="EnvironmentalImpactAssessment"),
            path('EIM', views.EnvironmentalIncidentManagement, name="EnvironmentalIncidentManagement"),
            path('ER', views.EnvironmentalReporting, name="EnvironmentalReporting"),
            path('EIAT', views.EnvironmentalImpactAssessmentTraining, name="EnvironmentalImpactAssessmentTraining"),
        ]
