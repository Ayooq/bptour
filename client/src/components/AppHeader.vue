<template>
  <q-header class="bp-header" elevated>
    <q-toolbar>
      <q-toolbar-title>
        <q-btn :to="{ name: 'home' }" class="bp-logo" dense flat rounded>
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

      <q-tabs v-model="tab" class="orientation-landscape" shrink stretch>
        <q-route-tab
          v-for="(item, index) in tabs"
          :key="index"
          :label="item[1]"
          :name="item[0]"
          :to="{ name: item[2], hash: item[3] }"
          exact
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
            v-for="(item, index) in tabs"
            :key="index"
            :to="{ name: item[2], hash: item[3] }"
            clickable
            exact
          >
            <q-item-section>{{ item[1] }}</q-item-section>
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
  data() {
    return {
      tabs: [
        ["home", "Главная", "home", ""],
        ["tours", "Туры", "home", "#tours"],
        ["contacts", "О нас", "home", "#contacts"],
        ["countries", "Страны", "countries", ""]
      ]
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
    }
  }
};
</script>

<style lang="stylus" scoped>
.bp-header
  background: linear-gradient(145deg, $primary 29%, $secondary 63%)
</style>
