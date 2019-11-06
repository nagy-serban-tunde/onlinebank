<template>
  <v-app>
    <div>
      <v-card dark height="60">
        <v-card-title primary-title class="justify-center">
          <v-header class="subtitle-0">Personal data</v-header>
        </v-card-title>
      </v-card>
      <v-list-item>
        <v-list-item-content>
          <v-row dense>
            <v-col>
              <v-card dark outlined max-width="300">
                <v-layout center>
                  <v-subheader class="subtitle-1">Name:</v-subheader>
                  <li v-for="user in users" :key="user.id">{{ user.name }}</li>
                </v-layout>
              </v-card>
              <v-card dark outlined max-width="300">
                <v-subheader class="subtitle-2">Birth date:</v-subheader>
              </v-card>
            </v-col>
            <v-col>
              <v-card dark outlined max-width="300">
                <v-subheader class="subtitle-3">E-mail:</v-subheader>
              </v-card>
              <v-card dark outlined max-width="300">
                <v-subheader class="subtitle-4">Summa:</v-subheader>
                <v-layout mr-5 justify-space-around>
                  <v-card-actions color="green">
                    <v-btn outlined color="success" text>Add</v-btn>
                  </v-card-actions>
                </v-layout>
              </v-card>
            </v-col>
          </v-row>
          <v-card dark outlined max-width="300">
            <v-subheader class="subtitle-5">Picture:</v-subheader>
            <v-layout>
              <img width="200px" src="https://randomuser.me/api/portraits/women/72.jpg" />
            </v-layout>
          </v-card>
        </v-list-item-content>
      </v-list-item>
    </div>
  </v-app>
</template>

<script>
export default {
  name: "DataSheet",
  props: ["dataSheet"]
};
</script>

<style scoped>
</style>