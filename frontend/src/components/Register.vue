<template>
  <div id="app">
    <v-app id="inspire" style="background-color: #333333">
      <v-card
        style="border-radius:7px"
        max-width="400"
        elevation="10"
        dark
        class="ma-auto"
        :loading="loadingCard"
      >
        <v-toolbar flat dark>
          <v-card-title>Register</v-card-title>
          <v-spacer></v-spacer>
        </v-toolbar>
        <v-container fluid grid-list-lg>
          <v-form ref="form" lazy-validation>
            <v-layout wrap>
              <v-layout>
                <v-flex>
                  <v-text-field
                    class="ml-5"
                    type="name"
                    name="name"
                    v-model="name"
                    label="Username"
                    color="green"
                    dense
                    :rules="[ value =>!! value || 'Username is required!']"
                  ></v-text-field>
                </v-flex>
                <v-flex>
                  <v-text-field
                    name="password"
                    v-model="password"
                    class="mr-5"
                    label="Password"
                    color="green"
                    :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
                    :type="show ? 'text' : 'password'"
                    counter="16"
                    @click:append="show = !show"
                    required
                    dense
                    :rules="[ value => value.length >= 5 || 'Min 5 characters']"
                  ></v-text-field>
                </v-flex>
              </v-layout>
              <v-flex xs12>
                <v-text-field
                  class="mx-3"
                  type="e-mail"
                  name="e-mail"
                  v-model="email"
                  label="E-mail"
                  color="green"
                  dense
                  :rules="[ value =>!! value || 'E-mail is required!']"
                />
              </v-flex>
              <v-dialog
                ref="dialog"
                v-model="modal"
                :return-value.sync="date"
                persistent
                width="290px"
              >
                <template v-slot:activator="{ on }">
                  <v-text-field
                    class="mx-5"
                    v-model="date"
                    label="Birth Date"
                    prepend-icon="fas fa-calendar-day"
                    readonly
                    color="green"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="date" dark scrollable>
                  <v-spacer></v-spacer>
                  <v-btn text @click="modal = false">Cancel</v-btn>
                  <v-btn text @click="$refs.dialog.save(date)">OK</v-btn>
                </v-date-picker>
              </v-dialog>
            </v-layout>
            <v-layout mx-4 justify-space-around>
              <v-select
                class="mr-5"
                :items="gendersList"
                label="Gender"
                color="green"
                item-color="green"
                :rules="[ value =>!! value || 'Gender is required!']"
              />
              <v-text-field
                type="phonenumber"
                name="phonenumber"
                v-model="phonenumber"
                label="Phone number"
                color="green"
                :rules="[ value =>!! value || 'Phone number is required!']"
              ></v-text-field>
            </v-layout>
            <v-checkbox
              v-model="checkbox"
              :rules="[value => !!value || 'You must agree to continue!']"
              label="Do you accept our Terms of services?"
              color="green"
              required
            ></v-checkbox>
            <v-layout justify-center align-center>
              <v-btn class="mt-3 mb-5" color="success" text @click="validateUser" outlined>Register</v-btn>
            </v-layout>
          </v-form>
        </v-container>
        <v-fab-transition>
          <v-btn
            @click="toLogin"
            v-show="!hidden"
            color="green"
            fab
            dark
            small
            absolute
            bottom
            left
            :loading="loadingButton"
          >
            <v-icon>fas fa-arrow-left</v-icon>
          </v-btn>
        </v-fab-transition>
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
      email: "",
      phonenumber: "",
      show: false,
      loadingCard: false,
      loadingButton: false,
      hidden: false,
      checkbox: false,
      date: new Date().toISOString().substr(0, 10),
      modal: false,
      gendersList: ["F", "M"]
    };
  },
  methods: {
    toLogin() {
      this.loadingButton = "success";
      setTimeout(
        () => (
          (this.loadingButton = false), this.$router.push({ path: "login" })
        ),
        500
      );
    },
    // User viladtion meghivja a registert, ha helyesek az adatok
    validateUser() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        this.registerUser();
      }
    },
    async registerUser() {
      this.hidden = true;
      setTimeout(() => (this.loadingCard = "green"), 200);
      const response = await AuthRequest.register({
        name: this.name,
        password: this.password
      });

      setTimeout(
        () => ((this.hidden = false), (this.loadingCard = false)),
        2000
      );
      console.log(response.data);
    }
  }
};
</script>

<style></style>