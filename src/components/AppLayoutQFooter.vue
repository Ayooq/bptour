<template>
  <q-footer class="bp-footer bg-blue-grey-10 shadow-21" elevated>
    <QFooterToolbar />
  </q-footer>
</template>

<script>
import QFooterToolbar from "components/QFooterToolbar";

export default {
  name: "AppLayoutQFooter",
  components: {
    QFooterToolbar
  }
};
</script>

<style lang="stylus" scoped>
.bp-footer
  color: $light
</style>
