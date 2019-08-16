<template>
  <q-drawer
    v-model="drawerLeft"
    class="drawer-left"
    content-class="q-pa-md bg-primary"
    side="left"
    elevated
    overlay
  >
    <p
      class="drawer-left drawer-left__heading q-py-md text-subtitle1 text-right"
    >
      Оставьте заявку, и мы подберём подходящие для Вас туры!
    </p>

    <q-form class="q-pa-md" @submit.prevent="onSubmit" @reset="onReset">
      <q-input
        v-model="formName"
        class="q-mb-sm"
        label="Ваше имя *"
        standout="text-secondary"
        bg-color="orange-3"
        bottom-slots
        dense
        hide-hint
        no-error-icon
        rounded
        :error="!isValidName"
      >
        <template #prepend>
          <q-icon class="q-mx-xs" name="fas fa-user-circle" />
        </template>
        <template #hint>
          <div class="drawer-left drawer-left__form-field_hint text-caption">
            Поле обязательно к заполнению.
          </div>
        </template>
        <template #error>
          <div class="drawer-left drawer-left__form-field_error text-caption">
            Данное значение поля недопустимо!
          </div>
        </template>
        <template v-if="formName" #append>
          <q-icon
            class="q-ml-sm cursor-pointer"
            name="fas fa-user-times"
            @click.stop="formName = null"
          />
        </template>
      </q-input>
      <q-input
        v-model="formEmail"
        debounce="1000"
        class="q-mb-sm"
        type="email"
        label="Электронная почта *"
        standout="text-secondary"
        bg-color="orange-2"
        bottom-slots
        dense
        hide-hint
        no-error-icon
        rounded
        :error="!isValidEmail"
      >
        <template #prepend>
          <q-icon class="q-mx-xs" name="fas fa-envelope-open-text" />
        </template>
        <template #hint>
          <div class="drawer-left drawer-left__form-field_hint text-caption">
            Поле обязательно к заполнению.
          </div>
        </template>
        <template #error>
          <div class="drawer-left drawer-left__form-field_error text-caption">
            Данное значение поля недопустимо!
          </div>
        </template>
        <template v-if="formEmail" #append>
          <q-icon
            class="q-mx-xs cursor-pointer"
            name="fas fa-trash"
            @click.stop="formEmail = null"
          />
        </template>
      </q-input>
      <q-input
        v-model="formTel"
        class="drawer-left drawer-left__form-field_no-validation q-mb-sm justify-between"
        type="tel"
        prefix="+7"
        mask="(###) ###-##-##"
        label="Номер телефона"
        standout="text-positive"
        bg-color="orange-3"
        dense
        rounded
      >
        <template #prepend>
          <q-icon class="q-mx-xs" name="fas fa-mobile-alt" />
        </template>
        <template v-if="formTel" #append>
          <q-icon
            class="q-mx-xs cursor-pointer"
            name="fas fa-phone-slash"
            @click.stop="formTel = null"
          />
        </template>
      </q-input>
      <q-input
        v-model="formDate"
        mask="##.##.####"
        label="Дата *"
        standout="text-secondary"
        bg-color="orange-2"
        bottom-slots
        dense
        hide-hint
        no-error-icon
        rounded
        :error="!isValidDate"
      >
        <template #prepend>
          <q-icon class="q-mx-xs cursor-pointer" name="far fa-calendar-check">
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
        <template #hint>
          <div class="drawer-left drawer-left__form-field_hint text-caption">
            Предполагаемая дата путешествия. Щёлкните по иконке календаря либо
            введите дату вручную.
          </div>
        </template>
        <template #error>
          <div class="drawer-left drawer-left__form-field_error text-caption">
            Заявки рассматриваются только для текущего и следующего календарных
            годов!
          </div>
        </template>
        <template v-if="formDate" #append>
          <q-icon
            class="q-mx-xs cursor-pointer"
            name="far fa-calendar-times"
            @click.stop="formDate = null"
          />
        </template>
      </q-input>
      <hr class="invisible" />
      <div class="row justify-between q-mt-xl">
        <q-btn
          :loading="loading1"
          class="col-auto"
          type="submit"
          label="Отправить"
          color="positive"
          glossy
          push
          rounded
        >
          <template v-slot:loading>
            <q-spinner-puff size="1.4em" />
          </template>
        </q-btn>
        <q-btn
          class="col-auto"
          type="reset"
          label="Сбросить"
          color="negative"
          glossy
          push
          rounded
        />
      </div>
    </q-form>
  </q-drawer>
</template>

<script>
import { setTimeout } from "timers";
export default {
  name: "QDrawerLeft",
  data() {
    return {
      formName: null,
      formEmail: null,
      formTel: null,
      formDate: null,
      loading1: false
    };
  },
  computed: {
    drawerLeft() {
      return this.$store.state.bp.drawerLeft;
    },
    isValidName() {
      let reCheck = /^[a-zA-zА-Яа-я]+(\s+[a-zA-zА-Яа-я]+)*\s*$/;

      return reCheck.test(this.formName) ? true : false;
    },
    isValidEmail() {
      let reCheck = /^\w+@[a-z]+\.(com|net|kz|ru)$/;

      return !this.formEmail || reCheck.test(this.formEmail) ? true : false;
    },
    isValidDate() {
      let reCheck = /^((0[^0]|[12]\d|3[01])\.(0[^0]|1[0-2])\.(20)?(19|20))?$/;

      return !(
        this.formDate && [8, 10].some(val => this.formDate.length === val)
      ) || reCheck.test(this.formDate)
        ? true
        : false;
    }
  },
  methods: {
    onSubmit() {
      if (!this.formName || !this.formEmail || !this.formDate) {
        return;
      }

      return this.simulateProgress(1);
    },
    onReset() {
      this.formName = null;
      this.formEmail = null;
      this.formTel = null;
      this.formDate = null;
    },
    simulateProgress(number) {
      // we set loading state
      this[`loading${number}`] = true;
      // simulate a delay
      setTimeout(() => {
        // we're done, we reset loading state
        this[`loading${number}`] = false;
      }, 3000);
      this.$store.commit("bp/updDrawerLeftState");
    }
  }
};
</script>

<style lang="stylus">
.drawer-left
  &__heading
    color: $dark

  &__form-field
    &_no-validation
      margin-bottom: 2em

  &__form-field_hint, &__form-field_error
    margin-top: -0.4em
</style>
