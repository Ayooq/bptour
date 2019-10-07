<template>
  <q-page class="flex no-scroll">
    <section class="details bg-light">
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
  min-width: 250px
  width: 100%
  height: 100%
  border-radius: 0
  color: $dark
  text-shadow: none
</style>
