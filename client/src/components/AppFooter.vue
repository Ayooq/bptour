<template>
  <q-footer class="bp-footer bg-dark shadow-21" elevated>
    <q-toolbar class="row justify-between">
      <q-btn
        v-scroll-to="'#page'"
        :to="{ name: this.$route.name }"
        class="bp-logo col-auto"
        dense
        flat
        rounded
      >
        <q-avatar class="on-left">
          <img
            class="bp-logo bp-logo__img"
            src="statics/app-logo-128x128.png"
          />
        </q-avatar>
        <span class="gt-xs">Наверх</span>
      </q-btn>
      <span class="col text-center">Все права защищены. &copy; 2019</span>
      <span class="col-auto">
        <span class="gt-xs">Наши соцсети:</span>
        <q-btn
          :href="this.whatsAppLink"
          class="text-light"
          type="a"
          target="_blank"
          icon="fab fa-whatsapp"
          flat
          round
        />
        <q-btn
          :href="this.instagramLink"
          class="text-light"
          type="a"
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
  props: {
    links: Object
  },
  data() {
    return {
      ...this.links
    };
  }
};
</script>
