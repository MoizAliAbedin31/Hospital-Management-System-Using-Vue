from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related



class Clinic(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 254)
    Telephone = models.CharField(max_length=50)
    Location = models.CharField(max_length=70)
    Password = models.CharField(max_length = 50, null=True, blank= True)
    OpeningTime = models.TimeField()
    ClosingTime = models.TimeField()


class Doctor(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 254)
    Mobile = models.CharField(max_length = 15)
    Password = models.CharField(max_length = 50, null=True, blank= True)
    Location = models.CharField(max_length=70)
    Cnic = models.CharField(max_length=15)
    Qualification = models.CharField(max_length=50)
    ClinicID = models.ForeignKey(Clinic, on_delete=models.CASCADE, blank = True, null = True)  


class Patient(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.EmailField(max_length = 254)
    Mobile = models.CharField(max_length = 15)
    Password = models.CharField(max_length = 50, null=True, blank= True)
    Location = models.CharField(max_length=70)
    Cnic = models.CharField(max_length=15)


class Appointment(models.Model):
    DoctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank = True, null = True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE, blank = True, null = True)
    Date = models.DateField()
    Time = models.TimeField()
    Status = models.CharField(max_length=30)


class AppointmentInfo(models.Model):
    Prescription = models.CharField(max_length=50)
    Medicine = models.CharField(max_length=50)
    AppointmentID = models.ForeignKey(Appointment, on_delete=models.CASCADE, blank = True, null = True)


class User(AbstractUser):
    user_type = models.CharField(max_length=50, default='null')




# class Appointment(models.Model):
#     """Contains info about appointment"""

#     class Meta:
#         unique_together = ('doctor', 'date', 'timeslot')

#     TIMESLOT_LIST = (
#         (0, '09:00 – 09:30'),
#         (1, '10:00 – 10:30'),
#         (2, '11:00 – 11:30'),
#         (3, '12:00 – 12:30'),
#         (4, '13:00 – 13:30'),
#         (5, '14:00 – 14:30'),
#         (6, '15:00 – 15:30'),
#         (7, '16:00 – 16:30'),
#         (8, '17:00 – 17:30'),
#     )

#     doctor = models.ForeignKey('Doctor',on_delete = models.CASCADE)
#     date = models.DateField(help_text="YYYY-MM-DD")
#     timeslot = models.IntegerField(choices=TIMESLOT_LIST)
#     patient_name = models.CharField(max_length=60)

#     def __str__(self):
#         return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctor, self.patient_name)

#     @property
#     def time(self):
#         return self.TIMESLOT_LIST[self.timeslot][1]


# class Doctor(models.Model):
#     """Stores info about doctor"""

#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     middle_name = models.CharField(max_length=20)
#     specialty = models.CharField(max_length=20)

#     def __str__(self):
#         return '{} {}'.format(self.specialty, self.short_name)

#     @property
#     def short_name(self):
#         return '{} {}.{}.'.format(self.last_name.title(), self.first_name[0].upper(), self.middle_name[0].upper())