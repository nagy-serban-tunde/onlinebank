<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" outlined color="success" text>Add</v-btn>
    </template>
    <v-card :loading="loading" class="px-5">
      <v-card-title>Uploading {{currency}}</v-card-title>

      <v-text-field class="mx-5 mb-5" label="Amount to upload" clearable counter="7" name="amount" v-model="amount"/>
      <v-text-field
        class="mx-5 mb-5"
        label="Password"
        :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
        :type="show ? 'text' : 'password'"
        counter="24"
        @click:append="show = !show"
        :rules="[rules.required, rules.min]"
        name = "password"
        v-model="password"
      />

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="adding" color="success" text>Add</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>

import AuthRequest from "@/services/AuthService";

export default {
  name: "ExchangeDialog",
  props: ["currency"],
  data() {
    return {
      password: "",
      amount: "",
      show: false,
      dialog: false,
      loading: false,
      rules: {
        required: value => !!value || "Password is equired",
        min: v => v.length >= 5 || "Min 8 characters"
      }
    };
  },
  methods: {
    async adding() {
      var new_deposit = 0;
      new_deposit = new_deposit + parseFloat(this.amount);
      const response = await AuthRequest.changedeposit({
        password : this.password,
        deposit: new_deposit
      });
      this.loading = 'success';
      setTimeout(() => (this.loading = false, this.dialog = false,this.password = "",this.amount = ""), 1000);
    }
    
  }
};
</script>
<style>
</style>