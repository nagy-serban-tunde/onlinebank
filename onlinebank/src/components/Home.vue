<template>
  <div id="app">
    <v-app id="inspire">
      <v-navigation-drawer v-model="drawer" permanent expand-on-hover>
        <v-list-item>
          <v-list-item-avatar>
            <v-img src="https://randomuser.me/api/portraits/women/35.jpg"></v-img>
          </v-list-item-avatar>

          <v-list-item-title class="subtitle-1">Nagy Tunde</v-list-item-title>

          <v-btn icon>
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </v-list-item>

        <v-divider />

        <v-list dense>
          <v-list-item v-for="item in items" :key="item.title" link>
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
    </v-app>
  </div>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      drawer: true,
      items: [
        { title: "Home", icon: "fas fa-home" },
        { title: "My Account", icon: "far fa-user" },
        { title: "Statistics", icon: "fas fa-chart-line" }
      ]
    };
  }
};
</script>

<style>
</style>