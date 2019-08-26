<template>
  <q-toolbar class="row">
    <q-toolbar-title class="col">
      <q-btn v-scroll-to="'#home'" class="bp-logo" dense flat rounded>
        <q-avatar class="on-left">
          <img
            class="bp-logo bp-logo__img"
            src="statics/app-logo-128x128.png"
          />
        </q-avatar>
        <span class="capitalize">Наверх</span>
      </q-btn>
    </q-toolbar-title>
    <span class="col">Все права защищены. &copy; 2019</span>
    <q-btn
      class="on-right text-light"
      icon="fab fa-instagram"
      flat
      disable
      round
      @click="goToAddress"
    />
  </q-toolbar>
</template>

<script>
export default {
  name: "QFooterToolbar",
  methods: {
    goToAddress() {
      // @TODO
    }
  }
};
</script>

<style lang="stylus"></style>
