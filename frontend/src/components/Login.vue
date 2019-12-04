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
                  @click:append="show = !show"
                  :rules="[value => !!value || 'Password is required', value => value.length >= 5 || 'Min 5 characters']"
                  prepend-icon="fas fa-lock"
                />
              </v-flex>
              <v-layout justify-space-around align-center>
                <v-icon icon></v-icon>
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
      <v-snackbar v-model="loginSuccesSnackbar" class="mb-5 green--text">
        {{ loginSuccesMsg }}
        <v-btn text @click="loginSuccesSnackbar = false">Close</v-btn>
      </v-snackbar>
      <v-snackbar v-model="loginFailedSnackbar" class="mb-5 red--text">
        {{ loginFailedMsg }}
        <v-btn text @click="loginFailedSnackbar = false">Close</v-btn>
      </v-snackbar>
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
      show: false,
      loginFailedMsg: "",
      loginSuccesMsg: "",
      loginFailedSnackbar: false,
      loginSuccesSnackbar: false
    };
  },
  methods: {
    toHome() {
      this.loadingCard = "success";
      setTimeout(
        () => ((this.loadingCard = false), this.$router.push({ path: "home" })),
        1000
      );
    },
    validateUser() {
      if (this.$refs.form.validate()) {
        this.loginUser();
      }
    },
    async loginUser() {
      this.loadingCard = "green";
      const response = await AuthRequest.verification({
        name: this.name,
        password: this.password
      });
      if (response.data.error) {
        this.loginFailedMsg = response.data.error;
        setTimeout(
          () => (this.loginSuccesSnackbar = false),
          (this.loginFailedSnackbar = true),
          1000
        );
      } else {
        this.loginSuccesMsg = "User " + this.name + " logged in!";
        setTimeout(
          () => (this.loginFailedSnackbar = false),
          (this.loginSuccesSnackbar = true),
          1000
        );
        localStorage.setItem("userid", response.data.message);
        this.toHome();
      }
      setTimeout(() => (this.loadingCard = false), 1000);
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