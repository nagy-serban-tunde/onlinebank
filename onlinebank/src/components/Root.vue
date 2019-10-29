<template>
  <div id="app">
    <v-app id="inspire">
      <v-layout>
        <v-navigation-drawer dark v-model="drawer" app permanent expand-on-hover color="rgba(36, 52, 75)">
          <v-list-item>
            <v-list-item-avatar>
              <v-img src="https://randomuser.me/api/portraits/women/35.jpg"></v-img>
            </v-list-item-avatar>

            <v-list-item-title class="subtitle-1">Nagy Tunde</v-list-item-title>

            <v-btn @click.stop="drawer = !drawer" icon>
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
      drawer: false,
      items: [
        { title: "Home", icon: "fas fa-home", route: "/home" },
        { title: "My Account", icon: "far fa-user", route: "/account" },
        { title: "Statistics", icon: "fas fa-chart-line", route: "/statistics" }
      ]
    };
  }
};
</script>

<style>
</style>