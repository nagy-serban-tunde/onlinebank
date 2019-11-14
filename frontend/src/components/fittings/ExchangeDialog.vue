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
          <div class="overline mb-4">Exchange</div>
          <v-list-item-title
            class="headline mb-1 red--text"
          >-{{exchange.signFrom}} {{exchange.amountFrom}}</v-list-item-title>
        </v-list-item-content>
        <v-list-item-action
          class="headline mt-5 pt-5 green--text"
        >+{{exchange.signTo}} {{exchange.amountTo}}</v-list-item-action>
        <v-list-item-icon>
          <v-icon>{{exchange.iconFrom}}</v-icon>
          <v-icon>{{arrow}}</v-icon>
          <v-icon>{{exchange.iconTo}}</v-icon>
        </v-list-item-icon>
      </v-list-item>

      <v-divider />
      <v-card-actions>
        <v-card-subtitle>{{exchange.date}}</v-card-subtitle>
        <v-spacer />
        <v-btn text @click="dialog = false">back</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "ExchangeDialog",
  props: ["exchange"],
  data() {
    return {
      dialog: false,
      arrow: "fas fa-long-arrow-alt-right"
    };
  }
};
</script>
<style>
</style>