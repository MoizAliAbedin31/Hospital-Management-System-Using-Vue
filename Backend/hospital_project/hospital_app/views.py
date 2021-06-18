from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



class ClinicDetail(viewsets.ModelViewSet):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class DoctorDetail(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientDetail(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class AppointmentDetail(APIView):
  
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk = pk)
        except Appointment.DoesNotExist:
            raise Http404


    def get(self, request, pk = None,  format = None):
        if pk:
            appointment = self.get_object(pk)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data)
        else:
            appointment = Appointment.objects.all()
            serializer = AppointmentSerializer(appointment, many = True)
            return Response(serializer.data)


    def post(self, request, pk = None, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class AppointmentInfoDetail(APIView):
    def get_object(self, pk):
        try:
            return AppointmentInfo.objects.get(pk = pk)
        except Appointment.DoesNotExist:
            raise Http404


    def get(self, request, pk = None,  format = None):
        if pk:
            appointment_info = self.get_object(pk)
            serializer = AppointmentInfoDetailSerializer(appointment_info)
            return Response(serializer.data)
        else:
            appointment_info = AppointmentInfo.objects.all()
            serializer = AppointmentInfoDetailSerializer(appointment_info, many = True)
            return Response(serializer.data)


    def post(self, request, pk = None, format=None):
        serializer = AppointmentInfoDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)