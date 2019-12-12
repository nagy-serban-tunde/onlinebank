<template>
  <v-dialog dark v-model="dialog" width="300">
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" outlined color="success" text>Add</v-btn>
    </template>
    <v-card :loading="loadingCard" class="px-5">
      <v-card-title>Add Notification</v-card-title>
      <v-form ref="form" lazy-validation>
        <v-text-field
          class="mx-5"
          type="limit"
          name="limit"
          v-model="limit"
          label="Rate"
          color="green"
          :rules="[ value => /^\d+(\.\d{1,2})?$/.test(value) || 'Invalid input number!']"
        ></v-text-field>
      </v-form>

      <v-divider />

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="validate" color="success" text>Add</v-btn>
        <v-btn text @click="dialog = false">Back</v-btn>
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
export default {
  name: "CreateNotificationDialog",
  data() {
    return {
      limit: 0,
      dialog: false,
      loadingCard: false,
      regFailedMsg: "",
      regSuccesMsg: "",
      regFailedSnackbar: false,
      regSuccesSnackbar: false
    };
  },
  methods: {
    validate() {
      this.regSuccesMsg = "Notification limit added!";
      this.$emit("select-event", this.limit);
      setTimeout(
        () => (this.regFailedSnackbar = false),
        (this.regSuccesSnackbar = true),
        1000
      );
      this.$refs.form.reset();
      this.loadingCard = "success";
      setTimeout(
        () => (
          (this.loadingCard = false),
          (this.regSuccesSnackbar = false),
          (this.dialog = false)
        ),
        1000
      );
    }
  }
};
</script>