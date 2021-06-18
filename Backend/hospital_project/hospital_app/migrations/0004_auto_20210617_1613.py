# Generated by Django 3.2.4 on 2021-06-17 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0003_auto_20210617_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Status', models.CharField(max_length=30)),
                ('DoctorID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.doctor')),
                ('PatientID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.patient')),
            ],
        ),
        migrations.AddField(
            model_name='appointmentinfo',
            name='AppointmentID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_app.appointment'),
        ),
    ]
