<template>
  <div>
    <v-list two-line subheader>
      <create-exchange-dialog />
      <v-list-item v-for="exchange in exchangesList" :key="exchange.id">
        <v-list-item-avatar>
          <v-icon v-text="exchange.iconTo"></v-icon>
        </v-list-item-avatar>
        <v-layout>
          <v-list-item-content>
            <v-list-item-title>{{exchange.from}} to {{exchange.to}}</v-list-item-title>
            <v-list-item-subtitle v-text="exchange.date"></v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-layout align-center justify-space-around title>
              <span
                style="width:100px; text-align:right"
              >{{exchange.signFrom}} {{exchange.amountFrom}}</span>
              <v-icon class="mx-2">{{arrow}}</v-icon>
              <span style="width:100px; text-align:left">{{exchange.signTo}} {{exchange.amountTo}}</span>
              <exchange-dialog/>
            </v-layout>
          </v-list-item-action>
        </v-layout>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import ExchangeDialog from "./ExchangeDialog";
import CreateExchangeDialog from "./CreateExchangeDialog";

export default {
  name: "ExchangeList",
  components: { ExchangeDialog, CreateExchangeDialog },
  props: ["exchangesList"],
  data() {
    return {
      arrow: "fas fa-long-arrow-alt-right"
    };
  }
};
</script>

<style scoped>
</style>