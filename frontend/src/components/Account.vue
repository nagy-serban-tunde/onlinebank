<template>
    <v-app>
        <data-sheet :dataSheet="dataSheet"/>
    </v-app>
</template>

<script>

import DataSheet from "./fittings/DataSheet";

export default {
    name: "Account",
    components: {DataSheet},
}
</script>

<style scoped>

</style>