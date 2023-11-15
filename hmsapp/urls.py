# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_medical_record/', views.add_medical_record, name='add_medical_record'),
    path('view_patients/', views.view_patients, name='view_patients'),
    path('update_patient/<int:patient_id>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('view_medical_records/<int:patient_id>/', views.view_medical_records, name='view_medical_records'),
    path('update_medical_record/<int:record_id>/', views.update_medical_record, name='update_medical_record'),
]
