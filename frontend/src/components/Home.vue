<template>
  <div>
    <v-layout ma-5 justify-space-between>
      <exchange-card v-for="card in deposit" :key="card.currency" :card="card" />
    </v-layout>
    <v-layout />
    <v-card dark class="mx-5 mt-5">
      <v-divider />
      <v-subheader class="subtitle-1 mt-5">Transactions</v-subheader>
      <transaction-list :transactionsList="transactionsList" />
    </v-card>
    <v-card dark class="mx-5">
      <v-divider />
      <v-subheader class="subtitle-1 mt-5">Exchanges</v-subheader>
      <exchange-list :exchangesList="exchangesList" />
    </v-card>
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
      deposit: null,
      transactionsList: [
        {
          id: "1",
          name: "Public Transport",
          icon: "fas fa-bus",
          amount: "30.5",
          date: "Sept 23, 2019",
          type: "red--text",
          sign: "-",
          attitude: "expense",
          comment: "kellet bagora"
        },
        {
          id: "2",
          name: "Food",
          icon: "fas fa-utensils",
          amount: "19.6",
          date: "Sept 10, 2019",
          type: "red--text",
          sign: "-",
          attitude: "expense",
          comment:
            "Ket csomag perec, egy doboz pastetom, sok laska s meg valami edesseg is"
        },
        {
          id: "3",
          name: "Housing",
          icon: "fas fa-home",
          amount: "320",
          date: "Sept 2, 2019",
          type: "red--text",
          sign: "-",
          attitude: "expense",
          comment: "kestem a rezsivel"
        },
        {
          id: "4",
          name: "Income",
          icon: "fas fa-coins",
          amount: "1000",
          date: "Aug 11, 2019",
          type: "green--text",
          sign: "+",
          attitude: "income",
          comment: "anyum kuldott"
        },
        {
          id: "5",
          name: "Shopping",
          icon: "fas fa-shopping-bag",
          amount: "142.9",
          date: "Aug 10, 2019",
          type: "red--text",
          sign: "-",
          attitude: "expense",
          comment: "kaposzta, paradicsom, s egy uveg Jack"
        }
      ],
      exchangesList: [
        {
          id: "1",
          from: "Euro",
          to: "GPB",
          signFrom: "€",
          signTo: "£",
          rate: "4.56",
          iconFrom: "fas fa-euro-sign",
          iconTo: "fas fa-pound-sign",
          amountFrom: "320",
          amountTo: "275.3",
          date: "Jul 2, 2019"
        },
        {
          id: "2",
          from: "Euro",
          to: "USD",
          signFrom: "€",
          signTo: "$",
          rate: "1.11",
          iconFrom: "fas fa-euro-sign",
          iconTo: "fas fa-dollar-sign",
          amountFrom: "110",
          amountTo: "122",
          date: "Jan 27, 2013"
        },
        {
          id: "3",
          from: "USD",
          to: "EURO",
          signTo: "€",
          signFrom: "$",
          rate: "4.71",
          iconFrom: "fas fa-dollar-sign",
          iconTo: "fas fa-euro-sign",
          amountFrom: "104",
          amountTo: "93.8",
          date: "Feb 19, 2018"
        },
        {
          id: "4",
          from: "GBP",
          to: "USD",
          signTo: "$",
          signFrom: "£",
          rate: "1.29",
          iconFrom: "fas fa-pound-sign",
          iconTo: "fas fa-dollar-sign",
          amountFrom: "980",
          amountTo: "1,262.8",
          date: "Dec 24, 2017"
        }
      ]
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