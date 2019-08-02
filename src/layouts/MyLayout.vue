<template>
  <q-layout view="hHh Lpr fff">
    <q-header class="bp-header" elevated reveal>
      <q-toolbar class="row justify-between font-primary">
        <q-toolbar-title class="col-auto">
          <q-btn
            class="bp-logo"
            dense
            flat
            rounded
            @click="drawerLeft = !drawerLeft"
          >
            <q-avatar class="on-left">
              <img
                class="bp-logo bp-logo__img"
                src="statics/app-logo-128x128.png"
              />
            </q-avatar>
            <span class="gt-xs q-ml-sm text-h5 text-secondary"
              >Бюро Путешествий</span
            >
          </q-btn>
        </q-toolbar-title>

        <div
          class="col-auto lt-sm row q-col-gutter-xs text-subtitle1 text-center"
        >
          <div class="col-auto">Бюро</div>
          <div class="col-8 text-right">Путешествий</div>
        </div>

        <span class="col gt-xs q-mr-xl text-h5 text-right text-brown-9"
          >+7(707)462-66-69</span
        >

        <q-btn
          class="text-brown-9"
          icon="fab fa-instagram"
          flat
          hidden
          round
          @click="drawerRight = !drawerRight"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="drawerLeft" side="left" overlay elevated>
      <div class="fit q-pa-md bg-orange-7 inset-shadow">
        <div
          class="q-my-sm font-primary text-subtitle1 text-brown-9 text-right"
        >
          Оставьте заявку, и мы подберём подходящие туры для Вас!
        </div>

        <q-form class="q-mt-md q-pa-md" @submit="onSubmit" @reset="onReset">
          <q-input
            v-model="formName"
            label="Ваше имя"
            bg-color="orange-3"
            color="yellow"
            standout="text-warning"
            clearable
            dense
            rounded
            lazy-rules
            :rules="[val => (val && val.length > 0) || '']"
          >
            <template v-slot:prepend>
              <q-icon name="person" />
            </template>
          </q-input>
          <q-input
            v-model="formEmail"
            type="email"
            label="Электронная почта"
            color="info"
            bg-color="orange-2"
            standout="text-warning"
            clearable
            dense
            rounded
            lazy-rules
            :rules="[]"
          >
            <template v-slot:prepend>
              <q-icon name="mail" />
            </template>
          </q-input>
          <q-input
            v-model="formTel"
            class="justify-between"
            type="tel"
            prefix="+7"
            mask="(###) ###-##-##"
            label="Номер телефона"
            color="secondary"
            bg-color="orange-3"
            standout="text-warning"
            dense
            fill-mask
            rounded
            lazy-rules
            :rules="[]"
          >
            <template v-slot:prepend>
              <q-icon name="phone" />
            </template>
          </q-input>
          <q-input
            v-model="formData"
            type="date"
            bg-color="orange-2"
            hint="Предполагаемая дата путешествия"
            dense
            rounded
            standout
          >
            <template v-slot:prepend>
              <q-icon name="event" />
            </template>
          </q-input>

          <div class="row justify-between q-mt-lg">
            <q-btn
              type="submit"
              :loading="loading"
              label="Отправить"
              color="accent"
              push
              @click="simulateProgress()"
            />
            <q-btn
              class="q-ml-sm"
              type="reset"
              label="Сбросить"
              color="negative"
              push
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
        <q-toolbar-title>
          <q-btn class="bp-logo" dense flat rounded @click="scrollToTop">
            <q-avatar class="on-left">
              <img
                class="bp-logo bp-logo__img"
                src="statics/app-logo-128x128.png"
              />
            </q-avatar>
            <span class="capitalize">Наверх</span>
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
      drawerRight: true,
      loading: false
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
.bp-header
  background: linear-gradient(145deg, $primary 28%, $warning 63%)

.bp-logo
  &__img
    animation: spin 1.2s ease-in-out

  ^[0]:hover &
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

.text-subtitle1
  line-height: 1.42rem
</style>
