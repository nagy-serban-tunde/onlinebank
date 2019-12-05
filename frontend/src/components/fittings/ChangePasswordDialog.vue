<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" outlined color="success" text>Change</v-btn>
    </template>
    <v-card :loading="loading" class="px-5">
      <v-card-title>Change Password</v-card-title>
      <v-form ref="form" lazy-validation>
        <v-text-field
          class="mx-5 mb-5"
          @keyup.enter="changepassword"
          label="Old password"
          :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
          :type="show ? 'text' : 'password'"
          counter="24"
          @click:append="show = !show"
          name="password"
          v-model="password"
          :rules="[rules.required, rules.min]"
        />

        <v-text-field
          class="mx-5 mb-5"
          @keyup.enter="changepassword"
          label="New password"
          :append-icon="show1 ? 'fas fa-eye' : 'fas fa-eye-slash'"
          :type="show1 ? 'text' : 'password'"
          counter="24"
          @click:append="show1 = !show1"
          name="new_password"
          v-model="new_password"
          :rules="[rules.required, rules.min]"
        />
      </v-form>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="changepassword" color="success" text>Change</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
    <v-snackbar v-model="regSuccesSnackbar" class="mb-5 green--text">
      {{ regSuccesMsg }}
      <v-btn text @click="regSuccesSnackbar = false">Close</v-btn>
    </v-snackbar>
    <v-snackbar v-model="regFailedSnackbar" class="mb-5 red--text">
      {{ regFailedMsg }}
      <v-btn text @click="regFailedSnackbar = false">Close</v-btn>
    </v-snackbar>
  </v-dialog>
</template>

<script>
import AuthRequest from "@/services/AuthService";

export default {
  name: "ChangePassword",
  data() {
    return {
      password: "",
      new_password: "",
      show: false,
      show1: false,
      dialog: false,
      loading: false,
      regFailedMsg: "",
      regSuccesMsg: "",
      regFailedSnackbar: false,
      regSuccesSnackbar: false,
      rules: {
        required: value => !!value || "Password is required",
        min: v => v.length >= 5 || "Min 5 characters"
      }
    };
  },
  methods: {
    async changepassword() {
      if (this.$refs.form.validate()) {
        const userid = localStorage.getItem("userid");
        const user = await AuthRequest.account(userid);
        if (user.password == this.password) {
          const response = await AuthRequest.changepassword({
            id: userid,
            new_password: this.new_password
          });
          if (response.data.error) {
            this.regFailedMsg = response.data.error;
            setTimeout(
              () => (this.regSuccesSnackbar = false),
              (this.regFailedSnackbar = true),
              1000
            );
          } else {
            this.regSuccesMsg = response.data.message;
            setTimeout(
              () => (this.regFailedSnackbar = false),
              (this.regSuccesSnackbar = true),
              1000
            );
            this.$refs.form.reset();
          }
          this.loading = "success";
          setTimeout(
            () => (
              (this.loading = false),
              (this.regSuccesSnackbar = false),
              (this.regFailedSnackbar = false),
              (this.dialog = false)
            ),
            1000
          );
        } else {
          this.regFailedMsg = "Wrong password!";
          setTimeout(
            () => (this.regSuccesSnackbar = false),
            (this.regFailedSnackbar = true),
            1000
          );
        }
      }
    }
  }
};
</script>
<style>
</style>