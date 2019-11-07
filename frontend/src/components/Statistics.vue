<template>
  <div id="app">
    <v-sheet color="rgba(0, 0, 0, .12)">
      <v-sparkline
        :value="value"
        line-width="1"
        color="rgba(255, 255, 255, .7)"
        height="100"
        padding="20"
        stroke-linecap="round"
        smooth
      >
        <template v-slot:label="item">${{ item.value }}</template>
      </v-sparkline>
    </v-sheet>
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