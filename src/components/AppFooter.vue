<template>
  <q-footer class="bp-footer bg-dark shadow-21" elevated>
    <q-toolbar class="row justify-between">
      <q-btn
        v-scroll-to="'#home'"
        class="bp-logo col-auto"
        dense
        flat
        rounded
        @click="changeTab('home')"
      >
        <q-avatar class="on-left">
          <img
            class="bp-logo bp-logo__img"
            src="statics/app-logo-128x128.png"
          />
        </q-avatar>
        <span class="gt-xs">Наверх</span>
      </q-btn>
      <span class="col-auto text-center">Все права защищены. &copy; 2019</span>
      <span class="col-auto text-center">
        Наш Инстаграм:
        <q-btn
          class="on-right text-light"
          type="a"
          href="https://www.instagram.com/buroput18/"
          target="_blank"
          icon="fab fa-instagram"
          flat
          round
        />
      </span>
    </q-toolbar>
  </q-footer>
</template>

<script>
export default {
  name: "AppFooter",
  computed: {
    tab: {
      get() {
        return this.$store.state.bp.tab;
      },
      set(val) {
        this.$store.commit("bp/updHeaderTabValue", val);
      }
    }
  },
  methods: {
    changeTab(val) {
      this.tab = val;
    }
  }
};
</script>
