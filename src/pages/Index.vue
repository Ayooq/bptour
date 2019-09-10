<template>
  <q-page class="flex transparent no-scroll bg-light">
    <section id="home" class="hero full-width">
      <VParallax />
    </section>

    <section class="tours relative-position fit bg-dark">
      <VCard />
      <VGallery />
    </section>

    <section id="contacts" class="contacts fit q-pa-xl bg-light">
      <h3 class="text-center">Контактная информация</h3>
      <VSplitter />
    </section>
  </q-page>
</template>

<script>
import VParallax from "components/VParallax";
import VCard from "components/VCard";
import VGallery from "components/VGallery";
import VSplitter from "components/VSplitter";

export default {
  name: "PageIndex",
  components: {
    VParallax,
    VCard,
    VGallery,
    VSplitter
  }
};
</script>

<style lang="stylus">
.hero
  color: $light

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
    color: $dark
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

    &_bg
      background: radial-gradient(ellipse at top, $primary 0, $deep-orange-12 100%)

  &__label
    background-color: $deep-orange-10

  &__caption
    padding: 0.5em 1em 1.2em
    background-color: rgba(0, 0, 0, 0.3)

  &__text
    margin-top: -0.7em
    color: $dark
    text-align: justify
</style>
