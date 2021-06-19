<template>
  <v-container id="regular-tables-view" fluid tag="section">
    <view-intro heading="Hospital Management Tables" />

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

     </v-container>
</template>


<script>
import axios from "axios";
import Add_Item_Dialog_Doctor from './Add_Item_Dialog_Doctor.vue';

export default { 
  name: "DoctorTablesView",
  components: {
    Add_Item_Dialog_Doctor,
  },
   data() {
    return {
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
      records_doctor: [],
      };
  },
  mounted() {

    axios
      .get("http://www.localhost:8000/hospital_app/api/doctor/")
      .then((resp) => {
        this.records_doctor = resp.data;
        console.log(this.records_doctor);
      });

      
  },
};
</script>