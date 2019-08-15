<template>
  <q-header class="bp-header" elevated>
    <QHeaderToolbar />
  </q-header>
</template>

<script>
import QHeaderToolbar from "components/QHeaderToolbar";

export default {
  name: "AppLayoutQHeader",
  components: {
    QHeaderToolbar
  }
};
</script>

<style lang="stylus" scoped>
.bp-header
  background: linear-gradient(145deg, $secondary 29%, $primary 63%)
</style>
