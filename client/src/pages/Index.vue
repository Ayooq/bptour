<template>
  <q-page class="flex no-scroll bg-light">
    <section class="hero full-width">
      <VParallax @change-route="changeRoute" />
    </section>

    <section class="tours fit bg-dark">
      <transition appear enter-active-class="animated slideInUp">
        <VHeroCard />
      </transition>
      <VGallery @change-route="changeRoute" />
    </section>

    <section id="contacts" class="contacts fit q-mt-xl bg-light">
      <h3 class="text-center">Контактная информация</h3>
      <VSplitter />
    </section>
  </q-page>
</template>

<script>
import VParallax from "components/VParallax";
import VHeroCard from "components/VHeroCard";
import VGallery from "components/VGallery";
import VSplitter from "components/VSplitter";
import changeRoute from "src/mixins/handleRouteChange.js";

export default {
  name: "PageIndex",
  components: {
    VParallax,
    VHeroCard,
    VGallery,
    VSplitter
  },
  mixins: [changeRoute]
};
</script>

<style lang="stylus">
.hero
  &__logo
    max-width: 15em
    max-height: 15rem

  &__subtitle
    margin-bottom: -0.7em
    margin-left: 4.7em

    @media (max-width: 25.9rem)
      margin: -0.7em 0 0.4em

  &__cta
    margin-top: 0.7em
    background-color: $primary
    font-size: 1.3em

.tours
  color: $warning
  text-align: center

  &__content
    border-radius: 0

    @media (min-width: $breakpoint-md-min)
      margin: -7rem 3rem 7rem
      border-radius: 0.9rem
      box-shadow: $shadow-24

      ~/__gallery
        margin-top: -7rem

    &_bg
      background: radial-gradient(ellipse at top, $primary 0, $deep-orange-12 100%)

  &__label
    &-bg
      padding: 5em 0
      background-color: $deep-orange-10

    &-header
      font-size: 5rem
      line-height: 1em

      @media (max-width: $breakpoint-sm-max)
        font-size: 4rem

      @media (max-width: $breakpoint-xs-max)
        font-size: 3rem

  &__caption
    padding: 0.4em 1em 1.3em
    background-color: rgba(0, 0, 0, 0.3)

  &__text
    margin-top: -0.7em
    color: $light
    text-align: justify

.contacts
  color: $dark
  text-shadow: none

  &__icon
    margin-left: -5px

  &__link
    color: $secondary
    text-decoration: none

    &:hover
      color: $info
</style>
