<template>
  <v-dialog dark v-model="dialog" width="400">
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on">
        <v-icon color="grey lighten-1">mdi-information</v-icon>
      </v-btn>
    </template>
    <v-card elevation="10" dark outlined>
      <v-list-item>
        <v-list-item-content>
          <div class="overline mb-4">{{ transaction.attitude }}</div>
          <v-list-item-title class="headline mb-1">{{transaction.name}}</v-list-item-title>
        </v-list-item-content>
        <v-list-item-action
          :class="[transaction.type]"
          class="headline mt-5 pt-5"
        >{{transaction.sign}} {{transaction.amount}} RON</v-list-item-action>
        <v-list-item-icon>
          <v-icon>{{transaction.icon}}</v-icon>
        </v-list-item-icon>
      </v-list-item>
      <v-card-text class="pl-4">"{{transaction.comment}}"</v-card-text>
      <v-divider />
      <v-card-actions class="justify-start">
        <v-card-subtitle>{{transaction.date}}</v-card-subtitle>
        <v-spacer />
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "ExchangeDialog",
  props: ["transaction"],
  data() {
    return {
      dialog: false,
    };
  },
};
</script>
<style/>