<template>
  <q-header class="bp-header" elevated>
    <q-toolbar>
      <q-toolbar-title shrink>
        <q-btn class="bp-logo" dense flat rounded @click="goHome">
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

      <q-tabs v-model="currentTab" class="orientation-landscape" shrink stretch>
        <q-route-tab
          :to="{ name: 'home' }"
          name="home"
          label="Главная"
          exact
          @click="changeTab('home')"
        />
        <q-route-tab
          :to="{ name: 'home', hash: '#tours' }"
          name="tours"
          label="Туры"
          @click="changeTab('tours')"
        />
        <q-route-tab
          :to="{ name: 'home', hash: '#contacts' }"
          name="contacts"
          label="О нас"
          @click="changeTab('contacts')"
        />
        <q-route-tab
          :to="{ name: 'countries' }"
          name="countries"
          label="Страны"
          @click="changeTab('countries')"
        />
      </q-tabs>

      <q-btn-dropdown class="orientation-portrait" auto-close flat stretch>
        <template #label>
          <div class="row items-center no-wrap">
            <div class="text-center">Навигация</div>
            <q-icon name="fas fa-road" right />
          </div>
        </template>
        <q-list>
          <q-item
            :to="{ name: 'home' }"
            clickable
            exact
            @click="changeTab('home')"
          >
            <q-item-section>Главная</q-item-section>
          </q-item>
          <q-item
            :to="{ name: 'home', hash: '#tours' }"
            clickable
            @click="changeTab('tours')"
          >
            <q-item-section>Туры</q-item-section>
          </q-item>
          <q-item
            :to="{ name: 'home', hash: '#contacts' }"
            clickable
            @click="changeTab('contacts')"
          >
            <q-item-section>О нас</q-item-section>
          </q-item>
          <q-item
            :to="{ name: 'countries' }"
            clickable
            @click="changeTab('countries')"
          >
            <q-item-section>Страны</q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>

      <q-btn
        :href="insta"
        class="on-right text-light gt-xs"
        type="a"
        target="_blank"
        icon="fab fa-instagram"
        flat
        round
      />
    </q-toolbar>
  </q-header>
</template>

<script>
export default {
  name: "AppHeader",
  props: {
    tab: String,
    insta: String
  },
  computed: {
    currentTab: {
      get() {
        return this.tab;
      },
      set(val) {
        this.$store.commit("bp/updHeaderTabValue", val);
      }
    }
  },
  methods: {
    goHome() {
      if (this.$route.fullPath !== "/") {
        this.$router.push("/");
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
.bp-header
  background: linear-gradient(145deg, $primary 29%, $secondary 63%)
</style>
