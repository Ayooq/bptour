<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <AppHeader :tab="tab" :insta="instagramLink" @change-tab="changeTab" />

    <!-- <AppDrawers /> -->

    <q-page-container>
      <router-view />
    </q-page-container>

    <AppFooter
      :links="{ whatsAppLink, instagramLink }"
      @change-tab="changeTab"
    />
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
  data() {
    return {
      instagramLink: "https://www.instagram.com/buroput18/",
      whatsAppLink: "https://wa.me/77074626669"
    };
  },
  computed: {
    tab() {
      return this.$store.state.bp.tab;
    }
  },
  methods: {
    changeTab(val) {
      this.$store.commit("bp/updHeaderTabValue", val);
    }
  }
};
</script>

<style lang="stylus">
.bg-light
  background-color: $light
  color: $light
  text-shadow: 1px 1px 1px $dark

.bg-dark
  background-color: $dark
  color: $light

.bp-logo
  &__title
    color: $light
    text-shadow: 1px 1px 1px $dark

  &__img
    animation: spin 1.2s ease-in-out

    ~/:hover &
      animation: spin-h 1.2s ease-in-out

    &_filled
      border: 1px solid $secondary
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
