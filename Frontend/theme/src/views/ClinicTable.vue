<template>
  <v-container id="regular-tables-view" fluid tag="section">
    <view-intro heading="Hospital Management Tables" />

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

  </v-container>

</template>

<script>
import axios from "axios";
import Add_Item_Dialog_Clinic from "./Add_Item_Dialog_Clinic.vue";

export default { 
  name: "ClinicTablesView",
  components: {
    Add_Item_Dialog_Clinic,
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
      records_clinic: [],
      };
  },
  mounted() {
    axios
      .get("http://www.localhost:8000/hospital_app/api/clinic/")
      .then((resp) => {
        this.records_clinic = resp.data;
        console.log(this.records_clinic);
      });

      },
};
</script>