from django.urls import re_path,path
from rest_framework import urlpatterns
from rest_framework import routers
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'hospital_app'



router = DefaultRouter()
router.register(r'api/clinic', views.ClinicDetail, basename='clinic')
router.register(r'api/doctor', views.DoctorDetail, basename='doctor')
router.register(r'api/patient', views.PatientDetail, basename='patient')


urlpatterns = [
    path(r"api/appointment/", AppointmentDetail.as_view()),
    path(r"api/appointment/<int:pk>", AppointmentDetail.as_view()),
    path(r'api/appointment-info/', AppointmentInfoDetail.as_view()),
    path(r'api/appointment-info/<int:pk>', AppointmentInfoDetail.as_view()),

]

urlpatterns += router.urls