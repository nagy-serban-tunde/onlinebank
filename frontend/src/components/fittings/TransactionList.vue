<template>
  <div>
    <v-app id="inspire">
      <v-card dark>
        <v-list two-line subheader>
          <v-subheader class="subtitle-1">Transactions</v-subheader>

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
                  <v-layout :class="[transaction.type]" mr-5 justify-space-around>{{transaction.sign}}{{transaction.cost}} RON</v-layout>
                  <v-btn icon>
                    <v-icon color="grey lighten-1">mdi-information</v-icon>
                  </v-btn>
                </v-layout>
              </v-list-item-action>
            </v-layout>
          </v-list-item>

          <v-divider inset></v-divider>

          <v-subheader class="subtitle-1">Exchanges</v-subheader>

          <v-list-item v-for="transaction in exchanges" :key="transaction.id">
            <v-list-item-avatar>
              <v-icon v-text="transaction.icon"></v-icon>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-text="transaction.title"></v-list-item-title>
              <v-list-item-subtitle v-text="transaction.subtitle"></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn icon>
                <v-icon color="grey lighten-1">mdi-information</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-card>
    </v-app>
  </div>
</template>

<script>
export default {
  name: "TransactionList",
  props: ["transactionsList"]
};
</script>

<style scoped>
</style>