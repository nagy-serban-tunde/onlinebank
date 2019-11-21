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
        :loading="loading"
      >
        <v-toolbar flat dark>
          <v-card-title>Login</v-card-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-container fluid grid-list-lg class="pt-3">
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
                @click="textfieldSelected=true"
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
                @click:append="show = !show"
                :rules="[rules.required, rules.min]"
                prepend-icon="fas fa-lock"
              />
            </v-flex>
            <v-layout justify-space-around align-center>
              <v-btn outlined class="mt-3 mb-5" color="success" text @click="toHome">Login</v-btn>
              <v-btn outlined class="mt-3 mb-5" color="success" text @click="toRegister">Register</v-btn>
            </v-layout>
          </v-layout>
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
      loading: false,
      rules: {
        required: value => !!value || "Password is equired",
        min: v => v.length >= 5 || "Min 5 characters"
      }
    };
  },
  methods: {
    async login() {
      this.loading = "green";
      const response = await AuthRequest.register({
        name: this.name,
        password: this.password
      });
      setTimeout(() => (this.loading = false), 2000);
      console.log(response.data);
    },

    toRegister() {
      this.loading = "success";
      setTimeout(
        () => ((this.loading = false), this.$router.push({ path: "register" })),
        1000
      );
    },
    toHome() {
      this.loading = "success";
      setTimeout(
        () => ((this.loading = false), this.$router.push({ path: "home" })),
        2000
      );
    }
  }
};
</script>

<style></style>