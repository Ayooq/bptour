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
      <!-- <p>
        <img
          src="assets/bp-logo-full.svg"
          style="width:30vw;max-width:300px;"
        />
      </p>-->
      <h4 class="error error__status">
        Похоже, Вы выбрали не тот маршрут...
        <strong>(404)</strong>
      </h4>
      <h6 class="error error__text">
        Не переживайте, мы готовы указать Вам верное направление! С нами Вы
        никогда не заблудитесь!
      </h6>
      <q-btn class="error error__button" rounded @click="$router.push('/')"
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
  &__content
    margin-right: 5vw

  &__status
    color: $dark

  &__text
    margin: -1em
    color: $dark

  &__button
    margin-top: 4em
    width: 150px
    background-color: $positive
    color: $light
</style>
