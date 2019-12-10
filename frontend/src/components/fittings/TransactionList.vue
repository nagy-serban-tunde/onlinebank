<template>
  <div>
    <v-fab-transition>
      <v-btn @click="openTransactionList" v-on="on" color="green" fab dark small absolute right top>
        <v-icon>{{moreButton}}</v-icon>
      </v-btn>
    </v-fab-transition>
    <v-list two-line subheader>
      <create-transcation-dialog @refresh-event="getTransactionList" />
      <v-list-item v-for="transaction in transactionsListSliced" :key="transaction.id">
        <v-list-item-avatar>
          <v-icon :color="transaction.type" v-text="transaction.icon"></v-icon>
        </v-list-item-avatar>
        <v-layout>
          <v-list-item-content>
            <v-list-item-title v-text="transaction.name"></v-list-item-title>
            <v-list-item-subtitle v-text="transaction.date"></v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-layout align-center title>
              <v-layout
                :class="[transaction.type]"
                mr-5
                justify-space-around
              >{{transaction.sign}} {{transaction.amount}} RON</v-layout>
              <transcation-dialog :transaction="transaction" />
            </v-layout>
          </v-list-item-action>
        </v-layout>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import TranscationDialog from "./TransactionDialog";
import CreateTranscationDialog from "./CreateTransactionDialog";
import AuthRequest from "@/services/AuthService";

export default {
  name: "TransactionList",
  components: { TranscationDialog, CreateTranscationDialog },
  data() {
    return {
      transactionsList: "",
      transactionsListSliced: "",
      transactionListElementCount: 5,
      btnUp: "fas fa-angle-up",
      moreButton: "fas fa-angle-down"
    };
  },
  methods: {
    async getTransactionList() {
      const userid = localStorage.getItem("userid");
      const transactionsList = await AuthRequest.gettransactionlist(userid);
      this.transactionsList = transactionsList;
      this.transactionsListSliced = transactionsList.slice(
        0,
        this.transactionListElementCount
      );
    },
    openTransactionList() {
      var tmpList = this.transactionsList;
      var tmpBtn = this. moreButton;
      this.transactionsList = this.transactionsListSliced;
      this. moreButton = this.btnUp;
      this.transactionsListSliced = tmpList;
      this.btnUp = tmpBtn;
    }
  },
  mounted() {
    this.getTransactionList();
  }
};
</script>

<style />