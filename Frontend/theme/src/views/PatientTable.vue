<template>
  <v-container id="regular-tables-view" fluid tag="section">
    <view-intro heading="Hospital Management Tables" />
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

    
     </v-container>
</template>


<script>
import axios from "axios";
import Add_Item_Dialog_Patient from './Add_Item_Dialog_Patient.vue';

export default { 
  name: "PatientTablesView",
  components: {
    Add_Item_Dialog_Patient,
  },
  data() {
      return {
      headers_patient: [
        { text: "F.Name", value: "First_name" },
        { text: "L.Name", value: "Last_name" },
        { text: "Email", value: "Email" },
        { text: "Mobile No", value: "Mobile" },
        { text: "Location", value: "Location" },
        { text: "CNIC", value: "Cnic" },
      ],
    records_patient:[],
    };
  },
  mounted() {
    
    axios
    .get("http://www.localhost:8000/hospital_app/api/patient/")
    .then((resp) => {
      this.records_patient = resp.data;
      console.log(this.records_patient);
    });
     },
};
</script>

