<template>
  <div id="app">
    <v-app id="inspire" style="background-color: #333333">
      <v-layout>
        <v-navigation-drawer dark :temporary="!mini" :mini-variant.sync="mini" app permanent>
          <v-list-item>
            <v-list-item-avatar>
              <v-img :src = profile_picture ></v-img>
            </v-list-item-avatar>
            <v-layout column align-center>
              <v-list-item-title class="subtitle-1">{{ full_name }}</v-list-item-title>
              <v-list-item-subtitle class="mt-1 green--text caption">{{ deposit }} lej</v-list-item-subtitle>
            </v-layout>

            <v-btn @click.stop="mini = !mini" icon>
              <v-icon>mdi-chevron-left</v-icon>
            </v-btn>
          </v-list-item>

          <v-divider />

          <v-list dense>
            <v-list-item v-for="item in items" :key="item.title" router :to="item.route" link>
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>

          <v-divider />

          <v-list dense>
            <v-list-item  router :to="logoutProps.route" link>
              <v-list-item-icon>
                <v-icon>{{ logoutProps.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ logoutProps.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-navigation-drawer>
        <v-container class="justify-center">
          <router-view />
        </v-container>
      </v-layout>
    </v-app>
  </div>
</template>

<script>

import AuthRequest from "@/services/AuthService";

export default {
  name: "Root",
  data() {
    this.user();
    return {
      mini: true,
      profile_picture: "",
      full_name: "",
      deposit: "",
      items: [
        { title: "Home", icon: "fas fa-home", route: "/home" },
        { title: "My Account", icon: "far fa-user", route: "/account" },
        { title: "Statistics", icon: "fas fa-chart-line", route: "/statistics" }
      ],
      logoutProps: {
        title: "Log Out",
        icon: "fas fa-power-off",
        route: "/login"
      },
    };
  },
   methods: {
      async user (){
        const response = await AuthRequest.account(2);
        this.profile_picture = response.profile_picture;
        this.full_name = response.full_name;
        this.deposit = response.deposit;
      },
  },
};
</script>

<style>
</style>