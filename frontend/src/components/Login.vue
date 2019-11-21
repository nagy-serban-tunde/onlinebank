<template>
  <div id="app">
    <v-app id="inspire" style="background-color: #333333">
      <v-card
        style="border-radius:7px"
        max-width="400"
        elevation="10"
        outlined
        dark
        class="ma-auto"
        :loading="loadingCard"
      >
        <v-toolbar flat dark>
          <v-card-title>Login</v-card-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-container fluid grid-list-lg class="pt-3">
          <v-form ref="form" lazy-validation>
            <v-layout row wrap>
              <v-flex>
                <v-text-field
                  class="mx-5"
                  type="name"
                  name="name"
                  v-model="name"
                  label="Username"
                  color="green"
                  prepend-icon="fas fa-user"
                  @keyup.enter="validateUser"
                  :rules="[value=> !!value || 'Username is required']"
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  name="password"
                  v-model="password"
                  class="mx-5"
                  label="Password"
                  color="green"
                  :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
                  :type="show ? 'text' : 'password'"
                  counter="24"
                  @keyup.enter="validateUser"
                  :rules="[value => !!value || 'Password is required', value => value.length >= 5 || 'Min 5 characters']"
                  prepend-icon="fas fa-lock"
                />
              </v-flex>
              <v-layout justify-space-around align-center>
                <v-btn
                  :loading="loadingButton"
                  
                  class="mt-3 mb-5"
                  color="success"
                  text
                  @click="toRegister"
                >Register</v-btn>
                <v-btn outlined class="mt-3 mb-5" color="success" text @click="validateUser">Login</v-btn>
              </v-layout>
            </v-layout>
          </v-form>
        </v-container>
      </v-card>
    </v-app>
  </div>
</template>

<script>
import AuthRequest from "@/services/AuthService";

export default {
  name: "Register",
  data() {
    return {
      name: "",
      password: "",
      show: false,
      loadingCard: false,
      loadingButton: false,
    };
  },
  methods: {
    toHome() {
      this.loadingCard = "success";
      setTimeout(
        () => ((this.loadingCard = false), this.$router.push({ path: "home" })),
        2000
      );
    },
    validateUser() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        this.loginUser();
      }
    },
    async loginUser() {
      this.loadingCard = "green";
      const response = await AuthRequest.register({
        name: this.name,
        password: this.password
      });
      setTimeout(() => (this.loadingCard = false), 2000);
      console.log(response.data);
      this.toHome();
    },

    toRegister() {
      this.loadingButton = "success";
      setTimeout(
        () => (
          (this.loadingButton = false), this.$router.push({ path: "register" })
        ),
        700
      );
    }
  }
};
</script>

<style></style>