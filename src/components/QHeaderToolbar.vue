<template>
  <q-toolbar>
    <q-toolbar-title shrink>
      <q-btn class="bp-logo" dense flat rounded @click="toggleDrawerLeft">
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
          <q-icon name="fas fa-road" right />
        </div>
      </template>
      <q-list>
        <q-item v-scroll-to="'#home'" clickable @click="tab = 'home'">
          <q-item-section>Главная</q-item-section>
        </q-item>
        <q-item v-scroll-to="'#tours'" clickable @click="tab = 'tours'">
          <q-item-section>Туры</q-item-section>
        </q-item>
        <q-item v-scroll-to="'#about'" clickable @click="tab = null">
          <q-item-section>О нас</q-item-section>
        </q-item>
        <q-item v-scroll-to="'#contacts'" clickable @click="tab = null">
          <q-item-section>Контакты</q-item-section>
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
      @click="toggleDrawerRight"
    />
  </q-toolbar>
</template>

<script>
export default {
  name: "QHeaderToolbar",
  computed: {
    drawerLeft: {
      get() {
        return this.$store.state.bp.drawerLeft;
      },
      set(val) {
        this.$store.commit("bp/updDrawerState", val);
      }
    },
    drawerRight: {
      get() {
        return this.$store.state.bp.drawerRight;
      },
      set(val) {
        this.$store.commit("bp/updDrawerState", val);
      }
    },
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
    toggleDrawerLeft() {
      return this.drawerLeft("l");
    },
    toggleDrawerRight() {
      return this.drawerRight("r");
    }
  }
};
</script>

<style lang="stylus"></style>
