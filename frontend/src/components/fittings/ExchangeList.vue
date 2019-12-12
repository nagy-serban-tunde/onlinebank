<template>
  <div>
    <v-fab-transition>
      <v-btn @click="openExchangeList" color="green" fab dark small absolute right top>
        <v-icon>{{moreButton}}</v-icon>
      </v-btn>
    </v-fab-transition>
    <v-list two-line subheader>
      <create-exchange-dialog />
      <v-list-item v-for="exchange in exchangesListSliced" :key="exchange.id">
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
              <exchange-dialog :exchange="exchange" />
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
import AuthRequest from "@/services/AuthService";

export default {
  name: "ExchangeList",
  components: { ExchangeDialog, CreateExchangeDialog },
  data() {
    return {
      exchangesList: "",
      exchangesListSliced: "",
      exchangesListElementCount: 5,
      arrow: "fas fa-long-arrow-alt-right",
      btnUp: "fas fa-angle-up",
      moreButton: "fas fa-angle-down"
    };
  },
  methods: {
    async getExchangeList() {
      const userid = localStorage.getItem("userid");
      const exchangesList = await AuthRequest.getexchangelist(userid);
      console.log(exchangesList);
      this.exchangesList = exchangesList;
      this.exchangesListSliced = exchangesList.slice(
        0,
        this.exchangesListElementCount
      );
    },
    openExchangeList() {
      var tmpList = this.transactionsList;
      var tmpBtn = this.moreButton;
      this.transactionsList = this.transactionsListSliced;
      this.moreButton = this.btnUp;
      this.transactionsListSliced = tmpList;
      this.btnUp = tmpBtn;
    }
  },
  mounted() {
    this.getExchangeList();
  }
};
</script>

<style scoped>
</style>