<template>
  <div>
    <v-layout wrap ma-5 justify-space-between>
      <exchange-card v-for="card in cards" :key="card.currency" :card="card" />
      
    </v-layout>
  </div>
</template>

<script>
import ExchangeCard from "./fittings/ExchangeCard";
import axios from "axios";

export default {
  name: "Home",
  components: { ExchangeCard },
  data() {
    return {
      user: null,
     cards:[
       {currency: "Euro", amount: "500", sign: "€" ,icon: "as fa-euro-sign", from_curreny: "RON", exchange: "4.76"},
       {currency: "GBP", amount: "200", sign: "£" ,icon: "fas fa-pound-sign", from_curreny: "RON", exchange: "5.50"},
       {currency: "USD", amount: "1000", sign: "$" ,icon: "fas fa-dollar-sign", from_curreny: "RON", exchange: "4.29"}
     ]
    };
  },
  created() {
    axios
      .get("/static/WebScraping.json")
      .then(resp => {
        this.user = resp.data;
      });
  }
};
</script>

<style scoped>
</style>