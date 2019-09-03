<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <AppHeader />

    <!-- <AppDrawers /> -->

    <q-page-container>
      <router-view />
    </q-page-container>

    <AppFooter />
  </q-layout>
</template>

<script>
import AppHeader from "components/AppHeader";
// import AppDrawers from "components/AppDrawers";
import AppFooter from "components/AppFooter";
export default {
  components: {
    AppHeader,
    // AppDrawers,
    AppFooter
  },
  methods: {
    // openURL,
  }
};
</script>

<style lang="stylus">
.bg-light
  background-color: $light
  color: $dark

.bg-dark
  background-color: $dark
  color: $light

.bp-logo
  &__title
    color: $dark

  &__img
    animation: spin 1.2s ease-in-out

    ~/:hover &
      animation: spin-h 1.2s ease-in-out

    &_filled
      background-color: $secondary

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
