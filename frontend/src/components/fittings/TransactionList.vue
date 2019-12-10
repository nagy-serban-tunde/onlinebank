<template>
  <div>
    <v-list two-line subheader>
      <create-transcation-dialog @refresh-event="getTransactionList" />
      <v-list-item v-for="transaction in transactionsList" :key="transaction.id">
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
      transactionsList: ""
    };
  },
  methods: {
    async getTransactionList() {
      const userid = localStorage.getItem("userid");
      const transactionsList = await AuthRequest.gettransactionlist(userid);
      this.transactionsList = transactionsList;
    }
  },
  mounted() {
    this.getTransactionList();
  }
};
</script>

<style />