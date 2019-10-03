<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <AppHeader
      :tab="tab"
      :insta="instagramLink"
      @change-tab="changeTab"
      @go-home="goHome"
    />

    <AppDrawers />

    <q-page-container>
      <transition name="fade">
        <router-view />
      </transition>
    </q-page-container>

    <AppFooter
      :links="{ whatsAppLink, instagramLink }"
      @change-tab="changeTab"
    />
  </q-layout>
</template>

<script>
import AppHeader from "components/AppHeader";
import AppDrawers from "components/AppDrawers";
import AppFooter from "components/AppFooter";
export default {
  components: {
    AppHeader,
    AppDrawers,
    AppFooter
  },
  data() {
    return {
      instagramLink: "https://www.instagram.com/buroput18/",
      whatsAppLink: "https://wa.me/77074626669"
    };
  },
  computed: {
    tab: {
      get() {
        return this.$store.state.bp.tab;
      },
      set(val) {
        this.$store.commit("bp/updHeaderTabValue", val);
      }
    },
    drawerLeft: {
      get() {
        return this.$store.state.bp.drawerLeft;
      },
      set(val) {
        this.$store.commit("bp/updDrawerState", val);
      }
    }
    //   drawerRight: {
    //     get() {
    //       return this.$store.state.bp.drawerRight;
    //     },
    //     set(val) {
    //       this.$store.commit("bp/updDrawerState", val);
    //     }
    //   },
  },
  methods: {
    changeTab(val) {
      this.tab = val;
    },
    changeDrawerState(drawerName) {
      this.$store.commit("bp/updDrawerState", drawerName);
    },
    goHome() {
      if (this.$route.fullPath !== "/") {
        this.$router.push("/");
      }
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

.fade-enter-active, .fade-leave-active
  transition: opacity 0.4s

.fade-enter, .fade-leave-to
  opacity: 0

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
