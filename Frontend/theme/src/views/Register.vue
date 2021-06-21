<template>
  <v-container
    id="register-view"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <material-card
          color="primary"
          icon="mdi-account-outline"
        >
          <template #title>
            Register 
          </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
               

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    color="purple"
                    label="First Name"
                    v-model="obj['First_name']"
                  />
                </v-col>

                <v-col
                   cols="12"
                  md="4"
                >
                  <v-text-field
                    color="purple"
                    label="Last Name"
                    v-model="obj['Last_name']"
                  />
                </v-col>

               <v-col
                   cols="12"
                  md="4"
                >
                <v-text-field
                    color="purple"
                    label="CNIC"
                     v-model="obj['Cnic']"
                  />
                </v-col>
                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    color="purple"
                    label="Email"
                    :rules="emailRules"
                    v-model="obj['Email']"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    color="purple"
                    label="Mobile Number"
                     v-model="obj['Mobile']"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-autocomplete
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
                   v-model="obj['Location']"
                ></v-autocomplete>
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    color="purple"
                    label="Speciality"
                    v-model="obj['Qualification']"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="4"
                >
                  <v-text-field
                    color="purple"
                    label="Clinic ID"
                    type="number"
                    v-model="obj['ClinicID']"
                  />
                </v-col>

                
                <v-col
                  cols="12"
                  md="9"
                  class="text-right"
                >
                  <v-btn
                    color="primary"
                    min-width="120"
                    @click="addData();"
                  >
                   Register
                  </v-btn>
                </v-col>
                <v-col
                  cols="12"
                  md="3"
                  class="text-right"
                >
                  <v-btn
                    color="primary"
                    min-width="120"
                    text
                    @click=" gotologin();  
                    dialog = false;"
                    
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
    data(){
      return{
        obj:{

        },
        reqRules: [(v) => !!v || "Name is required"],
        emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
      }
    },

    methods:{
         gotologin(){
   this.$router.push('/login'); 
      }

    }
   }
</script>
