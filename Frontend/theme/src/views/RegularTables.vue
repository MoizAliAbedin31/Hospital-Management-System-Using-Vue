<template>
  <v-container id="regular-tables-view" fluid tag="section">
    <view-intro heading="Hospital Management Tables" link="components/simple-tables" />

    <material-card
      icon="mdi-clipboard-text"
      icon-small
      title="Clinic Table"
      color="accent"
    >
      <v-data-table
        :headers="headers_clinic"
        :items="records_clinic"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </material-card>
    <Add_Item_Dialog_Clinic/>

    <div class="py-3" />

    <material-card
      dark
      icon="mdi-clipboard-plus"
      icon-small
      title="Doctor Table"
      color="accent"
    >
      <v-data-table
        :headers="headers_doctor"
        :items="records_doctor"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </material-card>
    <Add_Item_Dialog_Doctor/>

  <div class="py-3" />

  <material-card
      icon="mdi-clipboard-text"
      icon-small
      title="Patient Table"
      color="accent"
    >
      <v-data-table
        :headers="headers_patient"
        :items="records_patient"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </material-card>
    <Add_Item_Dialog_Patient/>


  <div class="py-3" />  
  <div class="py-3" />  
  <material-card
      dark
      icon="mdi-clipboard-plus"
      icon-small
      title="Appointment Table"
      color="accent"
    >
      <v-data-table
        :headers="headers_appointment"
        :items="records_appointment"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </material-card>
    <Add_Item_Dialog_Appointment/>

    <div class="py-3" />  
  <div class="py-3" />  
    <material-card
      icon="mdi-clipboard-text"
      icon-small
      title="Appointment Information Table"
      color="accent"
    >
      <v-data-table
        :headers="headers_appointment_info"
        :items="records_appointment_info"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </material-card>
    <Add_Item_Dialog_Appointment_Info/>


  </v-container>



</template>

<script>
import axios from "axios";
import Add_Item_Dialog_Clinic from "./Add_Item_Dialog_Clinic.vue";
import Add_Item_Dialog_Doctor from './Add_Item_Dialog_Doctor.vue';
import Add_Item_Dialog_Patient from './Add_Item_Dialog_Patient.vue';
import Add_Item_Dialog_Appointment from './Add_Item_Dialog_Appointment.vue';
import Add_Item_Dialog_Appointment_Info from './Add_Item_Dialog_Appointment_Info.vue';


export default { 
  name: "RegularTablesView",
  components: {
    Add_Item_Dialog_Clinic,
    Add_Item_Dialog_Doctor,
    Add_Item_Dialog_Patient,
    Add_Item_Dialog_Appointment,
    Add_Item_Dialog_Appointment_Info
  },
  data() {
    return {
      headers_clinic: [
        { text: "Name", value: "Name" },
        { text: "Email", value: "Email" },
        { text: "Telephone", value: "Telephone" },
        { text: "Location", value: "Location" },
        { text: "Opening Timings", value: "OpeningTime" },
        { text: "Closing Timings", value: "ClosingTime" },
      ],
      headers_doctor: [
        { text: "F.Name", value: "First_name" },
        { text: "L.Name", value: "Last_name" },
        { text: "Email", value: "Email" },
        { text: "Mobile No", value: "Mobile" },
        { text: "Location", value: "Location" },
        { text: "CNIC", value: "Cnic" },
        { text: "Speciality", value: "Qualification" },
        { text: "Clinic ID", value: "ClinicID" },
      ], 
      headers_patient: [
        { text: "F.Name", value: "First_name" },
        { text: "L.Name", value: "Last_name" },
        { text: "Email", value: "Email" },
        { text: "Mobile No", value: "Mobile" },
        { text: "Location", value: "Location" },
        { text: "CNIC", value: "Cnic" },
      ],

      headers_appointment: [
        { text: "Date", value: "Date" },
        { text: "Time", value: "Time" },
        { text: "Status", value: "Status" },
        { text: "Doctor ID", value: "DoctorID" },
        { text: "Patient ID", value: "PatientID" },
      ],

      headers_appointment_info: [
        { text: "Prescription", value: "Prescription" },
        { text: "Medicine", value: "Medicine" },
        { text: "Appointment ID", value: "AppointmentID" },
      ],
      records_clinic: [],
      records_doctor: [],
      records_patient:[],
      records_appointment:[],
      records_appointment_info:[]
    };
  },
  mounted() {
    axios
      .get("http://www.localhost:8000/hospital_app/api/clinic/")
      .then((resp) => {
        this.records_clinic = resp.data;
        console.log(this.records_clinic);
      });

    axios
      .get("http://www.localhost:8000/hospital_app/api/doctor/")
      .then((resp) => {
        this.records_doctor = resp.data;
        console.log(this.records_doctor);
      });


    axios
    .get("http://www.localhost:8000/hospital_app/api/patient/")
    .then((resp) => {
      this.records_patient = resp.data;
      console.log(this.records_patient);
    });


    axios
    .get("http://www.localhost:8000/hospital_app/api/appointment/")
    .then((resp) => {
      this.records_appointment = resp.data;
      console.log(this.records_appointment);
    });


     axios
    .get("http://www.localhost:8000/hospital_app/api/appointment-info/")
    .then((resp) => {
      this.records_appointment_info = resp.data;
      console.log(this.records_appointment_info);
    });


  },
};
</script>


