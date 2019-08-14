<template>
  <q-layout view="hHh Lpr fff" class="font-primary">
    <q-header class="bp-header" elevated>
      <q-toolbar>
        <q-toolbar-title shrink>
          <q-btn
            class="bp-logo"
            dense
            flat
            rounded
            @click="drawerLeft = !drawerLeft"
          >
            <q-avatar class="on-left">
              <img
                class="bp-logo bp-logo__img bp-logo__img_filled"
                src="statics/app-logo-128x128.png"
              />
            </q-avatar>
            <span class="gt-xs q-ml-sm text-h5 text-brown-8"
              >Бюро Путешествий</span
            >
          </q-btn>
        </q-toolbar-title>

        <q-space />

        <q-tabs
          v-if="isWideEnough"
          v-model="tab"
          :breakpoint="0"
          align="right"
          shrink
          stretch
        >
          <q-tab name="home" label="Главная" />
          <q-tab name="tours" label="Туры" />
          <q-tab name="info" label="Информация" />
        </q-tabs>
        <q-btn-dropdown v-else class="float-right" auto-close flat stretch>
          <template v-slot:label>
            <div class="row items-center no-wrap">
              <div class="text-center">Навигация</div>
              <q-icon right name="map" />
            </div>
          </template>
          <q-list link>
            <q-item clickable @click="tab = 'movies'">
              <q-item-section>Movies</q-item-section>
            </q-item>

            <q-item clickable @click="tab = 'photos'">
              <q-item-section>Photos</q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>

        <!-- <span class="col-auto gt-xs q-mr-xl text-h5 text-right text-secondary"
          >+7(707)462-66-69</span
        >-->

        <q-btn
          class="on-right text-secondary"
          icon="fab fa-instagram"
          flat
          round
          @click="drawerRight = !drawerRight"
        />
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="drawerLeft"
      content-class="q-pa-md bg-orange-7"
      side="left"
      overlay
      elevated
    >
      <p class="q-my-md text-subtitle1 text-brown-8 text-right">
        Оставьте заявку, и мы подберём подходящие для Вас туры!
      </p>

      <q-form class="q-mt-md q-pa-md" @submit="onSubmit" @reset="onReset">
        <q-input
          v-model="formName"
          label="Ваше имя *"
          class="q-mb-sm"
          bg-color="orange-3"
          standout="text-warning"
          clearable
          dense
          rounded
          lazy-rules
          :rules="[validationRules.name]"
        >
          <template v-slot:prepend>
            <q-icon name="person" />
          </template>
        </q-input>
        <q-input
          v-model="formEmail"
          type="email"
          label="Электронная почта *"
          class="q-mb-sm"
          bg-color="orange-2"
          standout="text-warning"
          clearable
          dense
          rounded
          lazy-rules
          :rules="[validationRules.email]"
        >
          <template v-slot:prepend>
            <q-icon name="mail" />
          </template>
        </q-input>
        <q-input
          v-model="formTel"
          class="q-mb-sm justify-between"
          type="tel"
          prefix="+7"
          mask="(###) ###-##-##"
          label="Номер телефона"
          bg-color="orange-3"
          standout="text-warning"
          clearable
          dense
          rounded
          lazy-rules
          :rules="[]"
        >
          <template v-slot:prepend>
            <q-icon name="phone" />
          </template>
        </q-input>
        <q-input
          v-model="formDate"
          bg-color="orange-2"
          hint="Предполагаемая дата
            путешествия"
          mask="##.##.##"
          label="Дата *"
          standout="text-warning"
          clearable
          dense
          rounded
          lazy-rules
          :rules="[validationRules.date]"
        >
          <template v-slot:prepend>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy
                ref="qDateProxy"
                anchor="center right"
                transition-show="scale"
                transition-hide="scale"
              >
                <q-date
                  v-model="formDate"
                  default-view="Months"
                  mask="DD-MM-YYYY"
                  minimal
                  @input="() => $refs.qDateProxy.hide()"
                />
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
        <hr class="invisible" />
        <div class="row justify-between q-mt-lg">
          <q-btn
            :loading="loading1"
            class="col-auto"
            type="submit"
            label="Отправить"
            color="primary"
            push
          />
          <q-btn
            class="col-auto"
            type="reset"
            label="Сбросить"
            color="negative"
            push
          />
        </div>
      </q-form>
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

    <q-footer class="bg-blue-grey-10 text-white shadow-21" elevated>
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
      drawerLeft: false,
      drawerRight: true,
      formName: null,
      formEmail: null,
      formTel: null,
      formDate: null,
      innerWidth: window.innerWidth,
      loading1: false,
      tab: "home",
      validationRules: {
        name(val) {
          let reCheck = /^[a-zA-zА-Яа-я]+(\s+[a-zA-zА-Яа-я]+)*\s*$/;
          const errorHint = "Допускаются только буквенные символы";

          if (val) {
            return reCheck.test(val) ? true : errorHint;
          }

          return "Заполните поле!";
        },
        email(val) {
          let reCheck = /^\w+@[a-z]+\.(com|net|kz|ru)$/;
          const errorHint = "Убедитесь в правильности введённого адреса";

          if (val) {
            return reCheck.test(val) ? true : errorHint;
          }

          return "Заполните поле!";
        },
        date(val) {
          let reCheck = /^((0[^0]|[12]\d|3[01])\.(0[^0]|1[0-2])\.(20)?(19|20))?$/;
          const errorHint =
            "Заявки рассматриваются только для текущего и следующего календарных годов";

          return reCheck.test(val) ? true : errorHint;
        }
      }
    };
  },
  computed: {
    isWideEnough() {
      return innerWidth > 400;
    }
  },
  methods: {
    // openURL,
    simulateProgress(number) {
      // we set loading state
      this[`loading${number}`] = true;
      // simulate a delay
      setTimeout(() => {
        // we're done, we reset loading state
        this[`loading${number}`] = false;
      }, 3000);
    },
    onSubmit() {
      return this.simulateProgress(1);
    },
    onReset() {
      this.formName = null;
      this.formEmail = null;
      this.formTel = null;
      this.formDate = null;
    },
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
  background: linear-gradient(145deg, $orange-7 29%, $primary 63%)

.bp-logo
  &__img
    animation: spin 1.2s ease-in-out

    &_filled
      background-color: $primary

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
