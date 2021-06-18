<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on"> New Appointment Details </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5"> Appointment Information </span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="Prescription"
                  v-model="obj['Prescription']"
                  :rules="reqRules"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field
                  v-model="obj['Medicine']"
                  label="Medicine"
                  :rules="reqRules"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field
                  v-model="obj['AppointmentID']"
                  label="Appointment ID"
                  :rules="reqRules"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="
              dialog = false;
              addData();
            "
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      dialog: false,
      obj: {
      },
      reqRules: [(v) => !!v || "Name is required"],
     
      
    };
  },
  methods: {
    addData() {
      console.log(this.obj);
      axios
        .post("http://www.localhost:8000/hospital_app/api/appointment-info/", this.obj)
        .then(
          function (response) {
            this.obj = response.data;
            console.log(this.obj);
          }.bind(this)
        );
    },
  },

  // watch: {
  //   dialog (val) {
  //     if (!val) return

  //     setTimeout(() => (this.dialog = false), 4000)
  //   },
  // },
};
</script>