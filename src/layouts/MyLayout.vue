<template>
  <q-layout view="hHh Lpr fff">
    <q-header
      class="bg-primary text-cyan-4 font-primary shadow-9"
      reveal
      elevated
    >
      <q-toolbar class="row justify-between">
        <q-toolbar-title class="col-auto bp-logo">
          <q-btn
            :ripple="{ color: 'white' }"
            dense
            flat
            rounded
            @click="drawerLeft = !drawerLeft"
          >
            <q-avatar class="on-left">
              <img
                class="bp-logo bp-logo__img"
                src="statics/app-avatar-38x38.png"
              />
            </q-avatar>
            <span class="bp-logo bp-logo__title q-ml-sm text-h5"
              >Бюро Путешествий</span
            >
          </q-btn>
        </q-toolbar-title>

        <span class="col gt-xs mobile-hide q-mr-xl text-h5 text-right"
          >+7(707)462-66-69</span
        >

        <q-btn
          icon="fab fa-instagram"
          flat
          hidden
          round
          @click="drawerRight = !drawerRight"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawerLeft" side="left" overlay elevated>
      <div class="column q-pa-md bg-primary">
        <div class="q-my-sm font-primary text-info text-right">
          Оставьте заявку, и мы подберём Вам подходящие туры!
        </div>

        <q-form class="q-mt-md q-pa-sm" @submit="onSubmit" @reset="onReset">
          <q-input
            v-model="formName"
            label="Ваше имя"
            color="info"
            bg-color="green-1"
            dense
            filled
            rounded
            lazy-rules
            :rules="[
              val => (val && val.length > 0) || 'Пожалуйста, заполните поле'
            ]"
          />
          <q-input
            v-model="formEmail"
            type="email"
            label="Электронная почта"
            color="warning"
            bg-color="green-1"
            dense
            filled
            lazy-rules
            :rules="[]"
          />
          <q-input
            v-model="formTel"
            type="tel"
            prefix="+7"
            mask="(###) ###-##-##"
            label="Номер телефона"
            color="secondary"
            bg-color="green-1"
            dense
            filled
            lazy-rules
            :rules="[]"
          />
          <q-input
            v-model="formData"
            class="q-mb-lg"
            type="date"
            bg-color="green-1"
            hint="Предполагаемая дата путешествия"
            dense
            filled
          >
            <template v-slot:prepend>
              <q-icon name="event" />
            </template>
          </q-input>

          <div>
            <q-btn type="submit" label="Отправить" color="secondary" />
            <q-btn
              type="reset"
              label="Сбросить"
              color="primary"
              flat
              class="q-ml-sm"
            />
          </div>
        </q-form>
      </div>
    </q-drawer>

    <q-drawer
      v-model="drawerRight"
      side="right"
      :width="200"
      :breakpoint="500"
      show-if-above
      overlay
      elevated
      hidden
    >
      <q-scroll-area class="fit">
        <q-list padding class="menu-list">
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="inbox" />
            </q-item-section>

            <q-item-section>Inbox</q-item-section>
          </q-item>

          <q-item active clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="star" />
            </q-item-section>

            <q-item-section>Star</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="send" />
            </q-item-section>

            <q-item-section>Send</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="drafts" />
            </q-item-section>

            <q-item-section>Drafts</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer
      class="bg-blue-grey-10 text-white font-primary shadow-21"
      elevated
    >
      <q-toolbar>
        <q-toolbar-title class="bp-logo">
          <q-btn :ripple="false" dense flat rounded @click="scrollToTop">
            <q-avatar class="on-left">
              <img
                class="bp-logo bp-logo__img"
                src="statics/app-avatar-38x38.png"
              />
            </q-avatar>
            <span class="bp-logo bp-logo__title capitalize">Наверх</span>
          </q-btn>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      formName: "",
      formEmail: "",
      formTel: "",
      formDate: "",
      drawerLeft: false,
      drawerRight: true
    };
  },
  methods: {
    // openURL,
    scrollToTop() {
      const c = document.documentElement.scrollTop || document.body.scrollTop;

      if (c > 0) {
        window.requestAnimationFrame(this.scrollToTop);
        window.scrollTo(0, c - c / 12);
      }
    }
  }
};
</script>

<style lang="stylus" scoped>
.bp-logo {
  &__img {
    animation: spin 1.2s ease-in-out;

    ^[0]:hover & {
      animation: spin-h 1.2s ease-in-out;
    }
  }
}

@keyframes spin {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(360deg);
  }
}

@keyframes spin-h {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
