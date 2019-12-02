<template>
  <div id="app">
    <v-app id="inspire" style="background-color: #333333">
      <v-layout>
        <v-navigation-drawer dark :temporary="!mini" :mini-variant.sync="mini" app permanent>
          <v-list-item>
            <v-list-item-avatar>
              <v-img :src="profile_picture"></v-img>
            </v-list-item-avatar>
            <v-layout column align-center>
              <v-list-item-title class="subtitle-1">{{ first_name }} {{ last_name }}</v-list-item-title>
              <v-list-item-subtitle class="mt-1 green--text caption">• online</v-list-item-subtitle>
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
            <v-list-item router :to="logoutProps.route" link>
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
      <v-bottom-navigation max-height="50" hidden grow dark fixed color="grey">
        <v-btn>
          <span>{{depositEUR}}</span>
          <v-icon>fas fa-euro-sign</v-icon>
        </v-btn>

        <v-btn>
          <span>{{depositGBP}}</span>
          <v-icon>fas fa-pound-sign</v-icon>
        </v-btn>

        <v-btn>
          <span>{{depositUSD}}</span>
          <v-icon>fas fa-dollar-sign</v-icon>
        </v-btn>
         <v-btn>
          <span>{{depositRON}}</span>
          <v-icon>RON</v-icon>
        </v-btn>
      </v-bottom-navigation>
    </v-app>
  </div>
</template>

<script>
import AuthRequest from "@/services/AuthService";

export default {
  name: "Root",
  data() {
    return {
      mini: true,
      profile_picture: "",
      first_name: "",
      last_name: "",
      depositRON: "",
      depositGBP: "",
      depositUSD: "",
      depositEUR: "",
      items: [
        { title: "Home", icon: "fas fa-home", route: "/home" },
        { title: "My Account", icon: "far fa-user", route: "/account" },
        { title: "Statistics", icon: "fas fa-chart-line", route: "/statistics" }
      ],
      logoutProps: {
        title: "Log Out",
        icon: "fas fa-power-off",
        route: "/login"
      }
    };
  },
  methods: {
    async getUserInfo() {
      const userid = localStorage.getItem('userid')
      const user = await AuthRequest.account(userid);
      const deposit = await AuthRequest.getdeposit(userid);
      this.profile_picture = user.profile_picture;
      this.last_name = user.last_name;
      this.first_name = user.first_name;
      this.depositRON = deposit[0].amount;
      this.depositEUR = deposit[1].amount;
      this.depositGBP = deposit[2].amount;
      this.depositUSD = deposit[3].amount;
    }
  },
  mounted() {
    this.getUserInfo();
  }
};
</script>

<style>
</style>