<template>
  <div>
    <v-layout ma-5 justify-space-between>
      <exchange-card v-for="card in deposit" :key="card.currency" :card="card" />
    </v-layout>
    <v-layout />
    <v-layout ma-5 />
    <v-card dark class="mx-5 mt-5">
      <v-divider />
      <v-subheader class="subtitle-1 mt-5">Transactions</v-subheader>
      <transaction-list />
    </v-card>
    <v-card dark class="mx-5 mb-5">
      <v-divider />
      <v-subheader class="subtitle-1 mt-5">Exchanges</v-subheader>
      <exchange-list />
    </v-card>
    <v-layout ma-5 />
    <v-layout />
  </div>
</template>

<script>
import ExchangeCard from "./fittings/ExchangeCard";
import TransactionList from "./fittings/TransactionList";
import ExchangeList from "./fittings/ExchangeList";
import AuthRequest from "@/services/AuthService";
import axios from "axios";

export default {
  name: "Home",
  components: { ExchangeCard, TransactionList, ExchangeList },
  data() {
    return {
      deposit: null
    };
  },
  methods: {
    async getCards() {
      const userid = localStorage.getItem("userid");
      const deposit = await AuthRequest.getcard(userid);
      this.deposit = deposit;
    }
  },
  mounted() {
    this.getCards();
  }
};
</script>

<style scoped>
</style>