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
        :rules="[rules.required, rules.min]"
      />

      <v-text-field
        class="mx-5 mb-5"
        label="New password"
        :append-icon="show1 ? 'fas fa-eye' : 'fas fa-eye-slash'"
        :type="show1 ? 'text' : 'password'"
        counter="24"
        @click:append="show1 = !show1"
        :rules="[rules.required, rules.min]"
      />

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn v-on="on" @click="changing" color="success" text>Change</v-btn>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ChangePassword",
  data() {
    return {
      show: false,
      show1:false,
      dialog: false,
      loading: false,
      rules: {
        required: value => !!value || "Password is equired",
        min: v => v.length >= 8 || "Min 8 characters"
      }
    };
  },
  methods: {
    changing() {
      this.loading = 'success';
      setTimeout(() => (this.loading = false, this.dialog = false), 2000);
    }
  }
};
</script>
<style>
</style>