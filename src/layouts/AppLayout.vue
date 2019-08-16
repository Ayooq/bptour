<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <AppLayoutQHeader />

    <AppLayoutQDrawers />

    <q-page-container>
      <router-view />
    </q-page-container>

    <AppLayoutQFooter />
  </q-layout>
</template>

<script>
import AppLayoutQHeader from "components/AppLayoutQHeader";
import AppLayoutQDrawers from "components/AppLayoutQDrawers";
import AppLayoutQFooter from "components/AppLayoutQFooter";
export default {
  components: {
    AppLayoutQHeader,
    AppLayoutQDrawers,
    AppLayoutQFooter
  },
  methods: {
    // openURL,
  }
};
</script>

<style lang="stylus">
.text-subtitle1
  line-height: 1.42rem

.bp-logo
  &__img
    animation: spin 1.2s ease-in-out

    &_filled
      background-color: $secondary

  &__title
    color: $dark

  ^[0]:hover &__img
    animation: spin-h 1.2s ease-in-out

@keyframes spin
  0%
    transform: rotate(0)

  100%
    transform: rotate(360deg)

@keyframes spin-h
  0%
    transform: rotate(0)

  100%
    transform: rotate(360deg)
</style>
