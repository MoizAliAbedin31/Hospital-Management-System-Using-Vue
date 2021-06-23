<template>
  <v-container id="login-view" fluid tag="section" class="hero">
    <!-- <v-avatar size="120" justify="center">
  <v-img
        :src="
          require('@/assets/Hospital_logo.png')"
      />
      </v-avatar> -->
    <v-row justify="center">
      <v-col cols="12" md="8">
        <material-card color="primary" icon="mdi-account-outline">
          <template #title> Login </template>

          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    color="purple"
                    label="Email"
                    :rules="emailRules"
                    v-model="obj['Email']"
                  />
                </v-col>

                <v-col cols="12" md="6">
                  <v-text-field
                    color="purple"
                    label="Password"
                    v-model="obj['Password']"
                  />
                </v-col>

                <v-col cols="12" md="6">
                  <v-autocomplete
                    :rules="reqRules"
                    v-model="obj['Location']"
                    :items="items"
                  ></v-autocomplete>
                </v-col>

                <v-col cols="12" md="11" class="text-right">
                  <v-btn color="primary" min-width="120" @click="addData()">
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
      obj: {
        Location: "Patient",
      },
      
      items: ["Clinic", "Patient", "Doctor"],
      reqRules: [(v) => !!v || "Name is required"],
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
    };
  },

  methods: {
    gotoregister() {
      this.$router.push("/register");
    },
  },
};
</script>


