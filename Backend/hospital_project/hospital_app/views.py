from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



class ClinicDetail(viewsets.ModelViewSet):

# def register():
#     data = req.body
#     user = User(data['usernam'],password, user_type)
#     data['id'] = user.id
#     if data['type'] == 'cliinic':
#         clinic = Clinic(data)
#     if data['typ']
 
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


class User(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Login(APIView):
    def post(self, request):
        try:
            # import pdb; pdb.set_trace()
            params = request.data
            serializer = UserSerializer(data = params)
            if serializer.is_valid(raise_exception = True):
                # return Response({'Result':True})
                if Clinic.objects.filter(Email=params['email']).exists() or Doctor.objects.filter(Email=params['email']).exists() or Patient.objects.filter(Email=params['email']).exists():
                   
                    if params['user_type'].lower() == 'clinic':
                        clinic = Clinic.objects.filter(Email=params['email'])
                        clinic_seliarizer = ClinicSerializer(clinic, many=True)
                        return Response(clinic_seliarizer.data)


                    elif params['user_type'].lower() == 'doctor':
                        doctor = Doctor.objects.filter(Email=params['email'])
                        doctor_seliarizer = DoctorSerializer(doctor, many=True)
                        return Response(doctor_seliarizer.data)
                    


                    elif params['user_type'].lower() == 'patient':
                        patient = Patient.objects.filter(Email=params['email'])
                        patient_seliarizer = PatientSerializer(patient, many=True)
                        return Response(patient_seliarizer.data)

                else:
                    return Response({'Error': 'No Records Found'})


        except Exception as e:
            return Response({'Error': str(e)})


