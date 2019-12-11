<template>
  <v-card elevation="10" dark outlined max-width="24%">
    <v-fab-transition>
      <v-btn
        color="yellow"
        fab
        dark
        small
        absolute
        :ripple="false"
        :disabled="!notification"
        bottom
        right
      >
        <v-icon>far fa-bell</v-icon>
      </v-btn>
    </v-fab-transition>
    <v-list-item>
      <v-list-item-content>
        <div class="overline my-3"></div>
        <v-list-item-title class="headline mb-1">{{card.currency}} - {{card.sign}}{{card.amount}}</v-list-item-title>
        <v-list-item-subtitle>
          <v-layout>
            <v-layout>{{ card.from_curreny }} to {{card.currency}}:</v-layout>
            <v-layout justify-end>{{card.exchange}}</v-layout>
          </v-layout>
        </v-list-item-subtitle>
      </v-list-item-content>
      <v-list-item-icon class="mt-5">
        <v-icon>{{card.icon}}</v-icon>
      </v-list-item-icon>
    </v-list-item>

    <v-card-actions color="green"></v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: "ExchangeCard",
  props: ["card"],
  data() {
    return {
      notification: false
    };
  },
  computed: {
    notificationIsActive() {
      this.notification = true;
    }
  }
};
</script>
<style scoped>
</style>