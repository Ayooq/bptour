<template>
  <q-drawer
    v-model="drawerLeft"
    class="drawer-left"
    content-class="q-pa-md bg-secondary"
    side="left"
    overlay
    elevated
  >
    <p
      class="drawer-left drawer-left__heading q-py-md text-subtitle1 text-right"
    >
      Оставьте заявку, и мы подберём подходящие для Вас туры!
    </p>

    <q-form
      class="drawer-left drawer-left__form q-pa-md"
      @submit="onSubmit"
      @reset="onReset"
    >
      <q-input
        v-model="formName"
        label="Ваше имя *"
        class="q-mb-sm"
        bg-color="orange-3"
        standout="text-primary"
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
        standout="text-info"
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
        standout="text-accent"
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
</template>

<script>
export default {
  name: "QDrawerLeft",
  data() {
    return {
      formName: null,
      formEmail: null,
      formTel: null,
      formDate: null,
      loading1: false,
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
    drawerLeft() {
      return this.$store.state.bp.drawerLeft;
    }
  },
  methods: {
    onSubmit() {
      return this.simulateProgress(1);
    },
    onReset() {
      this.formName = null;
      this.formEmail = null;
      this.formTel = null;
      this.formDate = null;
    }
  }
};
</script>

<style lang="stylus">
.drawer-left
  &__heading
    color: $dark
</style>
