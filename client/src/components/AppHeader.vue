<template>
  <q-header class="bp-header" elevated>
    <q-toolbar>
      <q-toolbar-title shrink>
        <q-btn class="bp-logo" dense flat rounded @click="$emit('go-home')">
          <transition appear enter-active-class="animated rotateIn">
            <q-avatar class="on-left" style="animation-delay: 0.2s">
              <img
                class="bp-logo bp-logo__img bp-logo__img_filled"
                src="statics/app-logo-128x128.png"
              />
            </q-avatar>
          </transition>
          <span class="bp-logo bp-logo__title gt-xs q-ml-sm text-h5"
            >Бюро Путешествий</span
          >
        </q-btn>
      </q-toolbar-title>

      <q-space />

      <q-tabs v-model="tab" class="orientation-landscape" shrink stretch>
        <q-tab
          name="home"
          label="Главная"
          exact
          @click="$emit('change-route', 'home')"
        />
        <q-tab
          name="tours"
          label="Туры"
          @click="$emit('change-route', 'home', '#tours')"
        />
        <q-tab
          name="contacts"
          label="О нас"
          @click="$emit('change-route', 'home', '#contacts')"
        />
        <q-tab
          name="countries"
          label="Страны"
          @click="$emit('change-route', 'countries')"
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
          <q-item clickable exact @click="$emit('change-route', 'home')">
            <q-item-section>Главная</q-item-section>
          </q-item>
          <q-item clickable @click="$emit('change-route', 'home', '#tours')">
            <q-item-section>Туры</q-item-section>
          </q-item>
          <q-item clickable @click="$emit('change-route', 'home', '#contacts')">
            <q-item-section>О нас</q-item-section>
          </q-item>
          <q-item clickable @click="$emit('change-route', 'countries')">
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
    insta: String
  },
  computed: {
    tab: {
      get() {
        return this.$store.state.bp.tab;
      },
      set(val) {
        this.$store.commit("bp/updHeaderTabValue", val);
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
.bp-header
  background: linear-gradient(145deg, $primary 29%, $secondary 63%)
</style>
