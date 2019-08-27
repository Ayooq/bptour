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

<style lang="stylus">
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
