<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" outlined color="success" text>Change</v-btn>
    </template>
    <v-card :loading="loading" class="px-5">
      <v-card-title>Change Password</v-card-title>

      <v-text-field
        class="mx-5 mb-5"
        label="Old password"
        :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
        :type="show ? 'text' : 'password'"
        counter="24"
        @click:append="show = !show"
        name= "password"
        v-model="password"
        :rules="[rules.required, rules.min]"
      />

      <v-text-field
        class="mx-5 mb-5"
        label="New password"
        :append-icon="show1 ? 'fas fa-eye' : 'fas fa-eye-slash'"
        :type="show1 ? 'text' : 'password'"
        counter="24"
        @click:append="show1 = !show1"
        name = "new_password"
        v-model="new_password"
        :rules="[rules.required, rules.min]"
      />

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="changing" color="success" text>Change</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
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
      show1:false,
      dialog: false,
      loading: false,
      rules: {
        required: value => !!value || "Password is required",
        min: v => v.length >= 5 || "Min 5 characters"
      }
    };
  },
  methods: {
    async changing() {
      const response = await AuthRequest.changepassword({
        password : this.password,
        new_password: this.new_password
      });
      this.loading = 'success';
      setTimeout(() => (this.loading = false, this.dialog = false), 1000);
    }
  }
};
</script>
<style>
</style>