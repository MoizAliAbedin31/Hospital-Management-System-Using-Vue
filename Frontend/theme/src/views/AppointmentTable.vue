<template>
  <v-container id="regular-tables-view" fluid tag="section">
    <view-intro heading="Hospital Management Tables"  />

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

    </v-container>

</template>

<script>
import axios from "axios";
import Add_Item_Dialog_Appointment from './Add_Item_Dialog_Appointment.vue';

export default { 
  name: "AppointmentTablesView",
  components: {
    Add_Item_Dialog_Appointment,
  },
  data() {
    return {

      headers_appointment: [
        { text: "Date", value: "Date" },
        { text: "Time", value: "Time" },
        { text: "Status", value: "Status" },
        { text: "Doctor ID", value: "DoctorID" },
        { text: "Patient ID", value: "PatientID" },
      ],
    records_appointment:[],

    };
  },
  mounted() {


    axios
    .get("http://www.localhost:8000/hospital_app/api/appointment/")
    .then((resp) => {
      this.records_appointment = resp.data;
      console.log(this.records_appointment);
    });

    },
};
</script>
