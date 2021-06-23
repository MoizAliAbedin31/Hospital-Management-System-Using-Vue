<template>
  <v-container id="register-view" fluid tag="section">
    <v-row justify="center">
      <v-col cols="12" md="8">
        <material-card color="primary" icon="mdi-account-outline">
          <template #title> Clinic Registration Form </template>

          <v-form>
            <v-container class="py-0">
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

                <v-col cols="12" md='6'>
                  <v-text-field
                    label="Email*"
                    v-model="obj['Email']"
                    :rules="emailRules"
                  ></v-text-field>
                </v-col>

                <v-col cols="12" md='6'>
                  <v-text-field
                          type="password"
                          label="Password"
                          v-model="obj['Password']" 
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

                <v-col cols="12" md="9" class="text-right">
                  <v-btn color="primary" min-width="120" @click="addData()">
                    Register
                  </v-btn>
                </v-col>
                <v-col cols="12" md="3" class="text-right">
                  <v-btn
                    color="primary"
                    min-width="120"
                    text
                    @click="
                      gotologin();
                      dialog = false;
                    "
                  >
                    Login
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      obj: {},
      reqRules: [(v) => !!v || "Name is required"],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    };
  },

  methods: {
    gotologin() {
      this.$router.push("/login");
    },
  },
};
</script>
