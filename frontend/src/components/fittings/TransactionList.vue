<template>
  <div>
    <v-list two-line subheader>
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
              >{{transaction.sign}}{{transaction.amount}} RON</v-layout>
              <transcation-dialog/>
            </v-layout>
          </v-list-item-action>
        </v-layout>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import TranscationDialog from "./TransactionDialog";

export default {
  name: "TransactionList",
  components: { TranscationDialog },
  props: ["transactionsList"]
};
</script>

<style scoped>
</style>