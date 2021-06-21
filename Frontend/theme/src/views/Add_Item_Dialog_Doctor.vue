<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on"> New Doctor </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Doctor Information </span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="First Name*"
                  v-model="obj['First_name']"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="obj['Last_name']"
                  label="Last Name"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="obj['Location']"
                  :rules="reqRules"
                  :items="[
                    'Karachi',
                    'Islamabad',
                    'Rawalpindi',
                    'Lahore',
                    'Peshawar',
                    'Hyderabad',
                  ]"
                  label="City"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Mobile"
                  v-model="obj['Mobile']"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="obj['Email']"
                  label="Email"
                  :rules="emailRules"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-autocomplete
                  v-model="obj['Qualification']"
                  :rules="reqRules"
                  :items="[
                    'Dermatologists',
                    'Ophthalmologists',
                    'Cardiologists',
                    'Gastroenterologists',
                    'Nephrologists',
                    'Urologists',
                    'Psychiatrists',
                    'Radiologists'
                  ]"
                  label="Speciality"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12" sm="6">
              <v-text-field
                  label="CNIC"
                  v-model="obj['Cnic']"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
                <v-text-field
                  label="Clinic ID"
                  v-model="obj['ClinicID']"
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
        OpeningTime: null,
        ClosingTime: null,
      },
      reqRules: [(v) => !!v || "Name is required"],
      menu1: false,
      menu2: false,
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    };
  },
  methods: {
    addData() {
      console.log(this.obj);
      axios
        .post("http://www.localhost:8000/hospital_app/api/doctor/", this.obj)
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