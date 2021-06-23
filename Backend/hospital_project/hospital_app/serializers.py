from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class ClinicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clinic
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    # Clinic_name = serializers.ReadOnlyField(source='ClinicID.Name')
    class Meta:
        model = Doctor
        fields = '__all__'
        # fields = ('id', 'First_name', 'Last_name', 'Email', 'Mobile', 'Location', 'Cnic', 'Qualification', 'ClinicID', 'Clinic_name')


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentInfoDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppointmentInfo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'password', 'user_type'] 


       


