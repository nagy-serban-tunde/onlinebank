<template>
  <v-dialog dark v-model="dialog" width="500">
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on">
        <v-icon color="grey lighten-1">mdi-information</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title primary-title>Exchange Dialog</v-card-title>

      <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "ExchangeDialog",
  data() {
    return {
      dialog: false
    };
  }
};
</script>
<style>
</style>