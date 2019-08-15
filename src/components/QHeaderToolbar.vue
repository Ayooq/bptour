<template>
  <q-toolbar>
    <q-toolbar-title shrink>
      <q-btn class="bp-logo" dense flat rounded @click="toggleDrawer('l')">
        <q-avatar class="on-left">
          <img
            class="bp-logo bp-logo__img bp-logo__img_filled"
            src="statics/app-logo-128x128.png"
          />
        </q-avatar>
        <span class="bp-logo bp-logo__title gt-xs q-ml-sm text-h5"
          >Бюро Путешествий</span
        >
      </q-btn>
    </q-toolbar-title>

    <q-space />

    <q-tabs
      v-model="tab"
      class="orientation-landscape"
      align="right"
      shrink
      stretch
    >
      <q-tab v-scroll-to="'#home'" name="home" label="Главная" />
      <q-tab v-scroll-to="'#tours'" name="tours" label="Туры" />
      <q-btn-dropdown name="info" label="Информация" auto-close flat stretch>
        <q-list>
          <q-item v-scroll-to="'#about'" clickable @click="tab = null">
            <q-item-section>О нас</q-item-section>
          </q-item>
          <q-item v-scroll-to="'#contacts'" clickable @click="tab = null">
            <q-item-section>Контакты</q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>
    </q-tabs>

    <q-btn-dropdown class="orientation-portrait" auto-close flat stretch>
      <template v-slot:label>
        <div class="row items-center no-wrap">
          <div class="text-center">Навигация</div>
          <q-icon right name="map" />
        </div>
      </template>
      <q-list>
        <q-item v-scroll-to="'#home'" clickable @click="tab = 'home'">
          <q-item-section>Главная</q-item-section>
        </q-item>
        <q-item v-scroll-to="'#tours'" clickable @click="tab = 'tours'">
          <q-item-section>Туры</q-item-section>
        </q-item>
        <q-item v-scroll-to="'#about'" clickable @click="tab = 'info'">
          <q-item-section>Информация</q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>

    <!-- <span class="col-auto gt-xs q-mr-xl text-h5 text-right text-secondary"
          >+7(707)462-66-69</span
    >-->

    <q-btn
      class="on-right text-light"
      icon="fab fa-instagram"
      flat
      disable
      round
      @click="toggleDrawer('r')"
    />
  </q-toolbar>
</template>

<script>
export default {
  name: "QHeaderToolbar",
  data() {
    return {
      tab: "home"
    };
  },
  methods: {
    toggleDrawer(side) {
      if (side === "l") {
        this.$store.commit("bp/UPDATE_DRAWER_LEFT_STATE");
      } else if (side === "r") {
        this.$store.commit("bp/UPDATE_DRAWER_RIGHT_STATE");
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
.bp-logo
  &__img
    animation: spin 1.2s ease-in-out

    &_filled
      background-color: $primary

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
