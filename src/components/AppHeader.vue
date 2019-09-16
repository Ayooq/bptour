<template>
  <q-header class="bp-header" elevated>
    <q-toolbar>
      <q-toolbar-title shrink>
        <q-btn
          v-scroll-to="'#home'"
          class="bp-logo"
          dense
          flat
          rounded
          @click="changeTab('home')"
        >
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
        <q-tab
          v-scroll-to="'#home'"
          name="home"
          label="Главная"
          @click="changeTab('home')"
        />
        <q-tab
          v-scroll-to="'#tours'"
          name="tours"
          label="Туры"
          @click="changeTab('tours')"
        />
        <q-tab
          v-scroll-to="'#contacts'"
          name="contacts"
          label="О нас"
          @click="changeTab('contacts')"
        />
      </q-tabs>

      <q-btn-dropdown class="orientation-portrait" auto-close flat stretch>
        <template v-slot:label>
          <div class="row items-center no-wrap">
            <div class="text-center">Навигация</div>
            <q-icon name="fas fa-road" right />
          </div>
        </template>
        <q-list>
          <q-item v-scroll-to="'#home'" clickable @click="changeTab('home')">
            <q-item-section>Главная</q-item-section>
          </q-item>
          <q-item v-scroll-to="'#tours'" clickable @click="changeTab('tours')">
            <q-item-section>Туры</q-item-section>
          </q-item>
          <q-item
            v-scroll-to="'#contacts'"
            clickable
            @click="changeTab('contacts')"
          >
            <q-item-section>О нас</q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>

      <q-btn
        :href="this.insta"
        class="on-right text-light"
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
    changeTab(val) {
      this.$emit("change-tab", val);
    }
  }
  // computed: {
  //   drawerLeft: {
  //     get() {
  //       return this.$store.state.bp.drawerLeft;
  //     },
  //     set(val) {
  //       this.$store.commit("bp/updDrawerState", val);
  //     }
  //   },
  //   drawerRight: {
  //     get() {
  //       return this.$store.state.bp.drawerRight;
  //     },
  //     set(val) {
  //       this.$store.commit("bp/updDrawerState", val);
  //     }
  //   },
  //   tab: {
  //     get() {
  //       return this.$store.state.bp.tab;
  //     },
  //     set(val) {
  //       this.$store.commit("bp/updHeaderTabValue", val);
  //     }
  //   }
  // },
  // methods: {
  //   toggleDrawerLeft() {
  //     return this.drawerLeft.setProperty("l");
  //   },
  //   toggleDrawerRight() {
  //     return this.drawerRight("r");
  //   }
  // }
};
</script>

<style lang="stylus" scoped>
.bp-header
  background: linear-gradient(145deg, $primary 29%, $secondary 63%)
</style>
