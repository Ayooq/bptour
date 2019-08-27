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

<style lang="stylus"></style>
