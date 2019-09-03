<template>
  <q-footer class="bp-footer bg-dark shadow-21" elevated>
    <q-toolbar class="row">
      <q-toolbar-title class="col">
        <q-btn v-scroll-to="'#home'" class="bp-logo" dense flat rounded>
          <q-avatar class="on-left">
            <img
              class="bp-logo bp-logo__img"
              src="statics/app-logo-128x128.png"
            />
          </q-avatar>
          <span class="gt-xs">Наверх</span>
        </q-btn>
      </q-toolbar-title>
      <span class="absolute-center text-center"
        >Все права защищены. &copy; 2019</span
      >
      <q-btn
        class="on-right text-light"
        type="a"
        href="https://www.instagram.com/buroput18/"
        target="_blank"
        icon="fab fa-instagram"
        flat
        round
      />
    </q-toolbar>
  </q-footer>
</template>

<script>
export default {
  name: "AppFooter"
  // methods: {
  //   goToAddress() {
  //     @TODO
  //   }
  // }
};
</script>
