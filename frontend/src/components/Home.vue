<template>
  <v-app>
    <v-layout ma-5 justify-space-between>
      <exchange-card v-for="card in cardsList" :key="card.currency" :card="card" />
    </v-layout>
    <transaction-list :transactionsList="transactionsList"/>
  </v-app>
</template>

<script>
import ExchangeCard from "./fittings/ExchangeCard";
import TransactionList from "./fittings/TransactionList";
import axios from "axios";

export default {
  name: "Home",
  components: { ExchangeCard, TransactionList },
  data() {
    return {
      cardsList: null,
      transactionsList: [
        {id: "1", name: "Public Transport", icon: "fas fa-bus", cost: "30.5", date: "Sept 23, 2019", tpye: "green lighten-1 green--text", sign: "-"},
        {id: "2", name: "Food", icon: "fas fa-utensils", cost: "19.6", date: "Sept 10, 2019", tpye: "red", sign: "-"},
        {id: "3", name: "Housing", icon: "fas fa-home", cost: "320", date: "Sept 2, 2019", tpye: "red", sign: "-"},
        {id: "4", name: "Income", icon: "fas fa-coins", cost: "1000", date: "Aug 11, 2019", tpye: "green", sign: "+"},
        {id: "5", name: "Shopping", icon: "fas fa-shopping-bag", cost: "142.9", date: "Aug 10, 2019", tpye: "red", sign: "-"}
      ]
    };
  },
  created() {
    axios.get("/static/WebScraping.json").then(resp => {
      this.cardsList = resp.data;
    });
  },
  updated() {
    axios.get("/static/WebScraping.json").then(resp => {
      this.cardsList = resp.data;
    });
  }
};
</script>

<style scoped>
</style>