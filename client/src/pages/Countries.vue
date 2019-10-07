<template>
  <q-page class="flex no-scroll bg-light" padding>
    <section class="details full-width">
      <VDetailsCard />
    </section>
  </q-page>
</template>

<script>
import VDetailsCard from "components/VDetailsCard";
export default {
  name: "Countries",
  components: {
    VDetailsCard
  }
};
</script>

<style lang="stylus">
.details
  color: $dark
  text-shadow: none
</style>
