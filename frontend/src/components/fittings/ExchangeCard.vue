<template>
  <v-card elevation="10" dark outlined max-width="300">
    <v-list-item three-line>
      <v-list-item-content>
        <div class="overline mb-4">{{ card.from_curreny }} to</div>
        <v-list-item-title class="headline mb-1">{{card.currency}} - {{card.sign}}{{card.amount}}</v-list-item-title>
        <v-list-item-subtitle>
          <v-layout>
            <v-layout>{{ card.from_curreny }} to {{card.currency}}:</v-layout>
            <v-layout justify-end>{{card.exchange}}</v-layout>
          </v-layout>
        </v-list-item-subtitle>
      </v-list-item-content>
      <v-list-item-icon>
        <v-icon>{{card.icon}}</v-icon>
      </v-list-item-icon>
    </v-list-item>

    <v-card-actions color="green">
      <exchange-card-dialog/>
    </v-card-actions>
  </v-card>
</template>
<script>
import ExchangeCardDialog from "./ExchangeCardDialog";
export default {
  name: "ExchangeCard",
  components: { ExchangeCardDialog },
  props: ["card"]
};
</script>
<style scoped>
</style>