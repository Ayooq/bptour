<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <AppHeader :insta="instagramLink" />

    <!-- <AppDrawers /> -->

    <q-page-container>
      <keep-alive>
        <router-view id="page" />
      </keep-alive>
    </q-page-container>

    <AppFooter :links="{ whatsAppLink, instagramLink }" />
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
  }
  // computed: {
  //   drawerLeft: {
  //     get() {
  //       return this.$store.state.bp.drawerLeft;
  //     },
  //     set(val) {
  //       this.$store.commit("bp/updDrawerState", val);
  //     }
  //   }
  //   drawerRight: {
  //     get() {
  //       return this.$store.state.bp.drawerRight;
  //     },
  //     set(val) {
  //       this.$store.commit("bp/updDrawerState", val);
  //     }
  //   },
  // },
  // methods: {
  //   changeDrawerState(drawerName) {
  //     this.$store.commit("bp/updDrawerState", drawerName);
  //   }
  // }
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

.fade-enter-active, .fade-leave-active
  transition: opacity 0.4s

.fade-enter, .fade-leave-to
  opacity: 0

.bp-logo
  &__title
    color: $light
    text-shadow: 1px 1px 1px $dark

  &__img
    ~/:hover &
      animation: spin 1.1s ease-in-out

    &_filled
      border: 1px solid $secondary
      background-color: $secondary

@keyframes spin
  100%
    transform: rotate(360deg)
</style>
