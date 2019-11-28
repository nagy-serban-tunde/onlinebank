<template>
  <div id="app">
    <v-card dark max-width="500">

      <v-card-title primary-title class="justify-center">
        <v-subheader class="display-1 white--text">Tranzactions a month</v-subheader>
      </v-card-title>

      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)">
          <v-sparkline :value="value" color = green height="100" >
            <template v-slot:label="item" >
              ${{ item.value }}
            </template>
          </v-sparkline>
        </v-sheet>
      </v-card-text>
  
      <v-divider></v-divider>
    </v-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value: [112, 455, 248, 335, 423, 446, 675, 510, 590, 610, 760]
    };
  }
};
</script>

<style scoped>
</style>