<template>
  <v-container id="regular-tables-view" fluid tag="section">
    <view-intro heading="Hospital Management Tables" />
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
import Add_Item_Dialog_Appointment_Info from './Add_Item_Dialog_Appointment_Info.vue';

export default { 
  name: "AppointmentDetailsTablesView",
  components: {
    Add_Item_Dialog_Appointment_Info
  },
  data() {
      return {

      headers_appointment_info: [
        { text: "Prescription", value: "Prescription" },
        { text: "Medicine", value: "Medicine" },
        { text: "Appointment ID", value: "AppointmentID" },
      ],
      records_appointment_info:[]
    };
  },

  mounted() {
    
     axios
    .get("http://www.localhost:8000/hospital_app/api/appointment-info/")
    .then((resp) => {
      this.records_appointment_info = resp.data;
      console.log(this.records_appointment_info);
    });


  },
};
</script>