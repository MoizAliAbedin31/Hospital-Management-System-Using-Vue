    <template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on"> New Appointment</v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Appointment Information </span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6">
                <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="false"
                    :return-value.sync="date"
                    transition="scale-transition"
                    offset-y
                    min-width="auto"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                        v-model="obj['Date']"
                        label="Select Date"
                        prepend-icon="mdi-calendar"
                        readonly
                        v-bind="attrs"
                        v-on="on"
                    ></v-text-field>
                    </template>
                    <v-date-picker
                    v-model="obj['Date']"
                    no-title
                    scrollable
                    >
                    <v-spacer></v-spacer>
                    <v-btn
                        text
                        color="primary"
                        @click="menu = false"
                    >
                        Cancel
                    </v-btn>
                    <v-btn
                        text
                        color="primary"
                        @click="$refs.menu.save(date)"
                    >
                        OK
                    </v-btn>
                    </v-date-picker>
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
            v-model="obj['Time']"
            label="Select Time"
            prepend-icon="mdi-clock-time-four-outline"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
          v-if="menu2"
          v-model="obj['Time']"
          full-width
          @click:minute="$refs.menu.save(time)"
        ></v-time-picker>
      </v-menu>
              </v-col>
              
              <v-col cols="12">
                <v-text-field
                  label="Status"
                  v-model="obj['Status']"
                ></v-text-field>
              </v-col>

              <v-col cols="12" sm="6">
                <v-text-field
                  v-model="obj['DoctorID']"
                  label="Doctor ID"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6">
               <v-text-field
                  v-model="obj['PatientID']"
                  label="Patient ID"
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
          Time: null,
          Date: null
      },
      reqRules: [(v) => !!v || "Name is required"],
      menu2: false,
      
    };
  },
  methods: {
    addData() {
      console.log(this.obj);
      axios
        .post("http://www.localhost:8000/hospital_app/api/appointment/", this.obj)
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