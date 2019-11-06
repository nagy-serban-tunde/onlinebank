<template>
  <div id="app">
    <v-app id="inspire" style="background-color: #333333">
      <v-layout>
        <v-navigation-drawer dark :temporary="!mini" :mini-variant.sync="mini" app permanent>
          <v-list-item>
            <v-list-item-avatar>
              <v-img src="https://randomuser.me/api/portraits/women/72.jpg"></v-img>
            </v-list-item-avatar>
            <v-layout column align-center>
              <v-list-item-title class="subtitle-1">{{user.name}}</v-list-item-title>
              <v-list-item-subtitle class="mt-1 green--text caption">{{user.deposit}} lej</v-list-item-subtitle>
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
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>fas fa-power-off</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>Log Out</v-list-item-title>
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
export default {
  name: "Root",
  data() {
    return {
      mini: true,
      items: [
        { title: "Home", icon: "fas fa-home", route: "/home" },
        { title: "My Account", icon: "far fa-user", route: "/account" },
        { title: "Statistics", icon: "fas fa-chart-line", route: "/statistics" }
      ],
      user: {
        name: "Nagy Tunde",
        email: "nagyserbantunde@gmail.com",
        birthdate: "1997-01-11",
        deposit: "1467.4"
      }
    };
  }
};
</script>

<style>
</style>