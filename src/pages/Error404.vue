<template>
  <div class="error">
    <img
      class="error error__bg fit absolute"
      src="statics/images/plane.jpg"
      alt="bg"
    />
    <div
      class="error error__content fixed-right font-primary text-center transparent"
    >
      <h4 class="error error__status q-mx-lg">
        Похоже, Вы выбрали не тот маршрут...
        <strong>(404)</strong>
      </h4>
      <h6 class="error error__text q-mx-lg">
        Не переживайте, мы готовы указать Вам верное направление! С нами Вы
        никогда не заблудитесь!
      </h6>
      <q-btn
        class="error error__button"
        glossy
        rounded
        @click="$router.push('/')"
        >На главную</q-btn
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "Error404"
};
</script>

<style lang="stylus" scoped>
.error
  &__status, &__text
    color: $dark

  &__button
    margin-top: 2em
    width: 150px
    background-color: $primary
    color: $light
</style>
