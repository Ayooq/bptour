<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <AppLayoutQHeader />

    <QDrawerLeft />
    <QDrawerRight />

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="bg-blue-grey-10 text-white shadow-21" elevated>
      <q-toolbar>
        <q-toolbar-title>
          <q-btn class="bp-logo" dense flat rounded @click="scrollToTop">
            <q-avatar class="on-left">
              <img
                class="bp-logo bp-logo__img"
                src="statics/app-logo-128x128.png"
              />
            </q-avatar>
            <span class="capitalize">Наверх</span>
          </q-btn>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
import AppLayoutQHeader from "components/AppLayoutQHeader";
import QDrawerLeft from "components/QDrawerLeft";
import QDrawerRight from "components/QDrawerRight";
export default {
  components: {
    AppLayoutQHeader,
    QDrawerLeft,
    QDrawerRight
  },
  methods: {
    // openURL,
    simulateProgress(number) {
      // we set loading state
      this[`loading${number}`] = true;
      // simulate a delay
      setTimeout(() => {
        // we're done, we reset loading state
        this[`loading${number}`] = false;
      }, 3000);
    },

    scrollToTop() {
      const c = document.documentElement.scrollTop || document.body.scrollTop;

      if (c > 0) {
        window.requestAnimationFrame(this.scrollToTop);
        window.scrollTo(0, c - c / 12);
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
.text-subtitle1
  line-height: 1.42rem
</style>
