<template>
  <div class="bp-drawers">
    <QDrawerLeft />
    <QDrawerRight />
  </div>
</template>

<script>
import QDrawerLeft from "components/QDrawerLeft";
import QDrawerRight from "components/QDrawerRight";

export default {
  name: "AppDrawers",
  components: {
    QDrawerLeft,
    QDrawerRight
  }
};
</script>

<style lang="stylus" scoped></style>
