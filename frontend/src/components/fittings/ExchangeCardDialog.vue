<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn v-on="on" outlined color="success" text>Add</v-btn>
    </template>
    <v-card :loading="loading" class="px-5">
      <v-card-title>Uploading {{currency}}</v-card-title>

      <v-text-field class="mx-5 mb-5" label="Amount to upload" clearable counter="7" />
      <v-text-field
        class="mx-5 mb-5"
        label="Password"
        :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
        :type="show ? 'text' : 'password'"
        counter="24"
        @click:append="show = !show"
        :rules="[rules.required, rules.min]"
      />

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn v-on="on" @click="adding" color="success" text>Add</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "ExchangeDialog",
  props: ["currency"],
  data() {
    return {
      show: false,
      dialog: false,
      loading: false,
      rules: {
        required: value => !!value || "Password is equired",
        min: v => v.length >= 8 || "Min 8 characters"
      }
    };
  },
  methods: {
    adding() {
      this.loading = 'success';
      setTimeout(() => (this.loading = false, this.dialog = false), 2000);
    }
  }
};
</script>
<style>
</style>