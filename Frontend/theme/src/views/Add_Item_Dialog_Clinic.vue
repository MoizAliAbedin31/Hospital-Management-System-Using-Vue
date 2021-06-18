    <template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on"> New Clinic </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Clinic Information </span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  label="Name"
                  v-model="obj['Name']"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="obj['Telephone']"
                  label="Telephone"
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
              <v-col cols="12">
                <v-text-field
                  label="Email*"
                  v-model="obj['Email']"
                  :rules="emailRules"
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="6">
                 <v-menu
                ref="menu"
                v-model="menu1"
                :close-on-content-click="false"
                :nudge-right="40"
                :return-value.sync="time"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
            >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="obj['OpeningTime']"
            label="Opening Time"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="menu1"
          v-model="obj['OpeningTime']"
          full-width
          @click:minute="$refs.menu.save(time)"
        ></v-time-picker>
      </v-menu>
              </v-col>
              <v-col cols="12" sm="6">
               <v-menu
                ref="menu"
                v-model="menu2"
                :close-on-content-click="false"
                :nudge-right="40"
                :return-value.sync="time"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="290px"
            >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="obj['ClosingTime']"
            label="Closing Time"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="menu2"
          v-model="obj['ClosingTime']"
          full-width
          @click:minute="$refs.menu.save(time)"
        ></v-time-picker>
      </v-menu>
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
        OpeningTime : null,
        ClosingTime : null
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
        .post("http://www.localhost:8000/hospital_app/api/clinic/", this.obj)
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