<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" text>
        <span>{{amountprop}}</span>
        <v-icon>{{iconprop}}</v-icon>
      </v-btn>
    </template>
    <v-card :loading="loading" class="px-5">
      <v-card-title>
        Uploading
        <v-icon class="ml-3">{{iconprop}}</v-icon>
      </v-card-title>
      <v-form ref="form" lazy-validation>
        <v-layout mx-5>
          <v-flex md2 mr-5>
            <v-text-field readonly :value="amountprop + ' +'"></v-text-field>
          </v-flex>
          <v-flex>
            <v-text-field
              class="mb-5"
              label="Amount"
              color="green"
              clearable
              counter="10"
              hint="Up to 3 decimal places allowed"
              name="amount"
              :rules="[ value => /^\d+(\.\d{1,3})?$/.test(value) || 'Invalid input number!']"
              v-model="amount"
            />
          </v-flex>
        </v-layout>
        <v-text-field
          class="mx-5 mb-5"
          label="Password"
          color="green"
          :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
          :type="show ? 'text' : 'password'"
          counter="24"
          @click:append="show = !show"
          :rules="[value => !!value || 'Password is required', value => value.length >= 5 || 'Min 5 characters']"
          name="password"
          v-model="password"
        />
      </v-form>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="adding" color="success" text>Add</v-btn>
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
  name: "UploadMoney",
  props: ["iconprop", "amountprop", "currencyprop"],
  data() {
    return {
      password: "",
      amount: "",
      show: false,
      dialog: false,
      loading: false,
      regFailedMsg: "",
      regSuccesMsg: "",
      regFailedSnackbar: false,
      regSuccesSnackbar: false,
      actualcurrency: this.currencyprop
    };
  },
  methods: {
    async adding() {
      if (this.$refs.form.validate()) {
        const userid = localStorage.getItem("userid");
        const deposit = await AuthRequest.getdeposit(userid);
        const user = await AuthRequest.account(userid);
        if (this.password == user.password) {
          const currency = this.actualcurrency;
          const old_deposit = deposit[`${currency}`];

          var new_deposit = old_deposit + parseFloat(this.amount);
          const response = await AuthRequest.changedeposit({
            id: userid,
            new_deposit: new_deposit,
            currency: currency
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
            this.$emit("refresh-event");
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
          this.$refs.form.reset();
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