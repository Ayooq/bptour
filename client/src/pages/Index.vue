<template>
  <q-page class="flex transparent no-scroll bg-light">
    <section id="home" class="hero full-width">
      <VParallax @scrollto="handleScroll" />
    </section>

    <section class="tours fit bg-dark">
      <transition name="slide-up">
        <VCard />
      </transition>
      <VGallery @scrollto="handleScroll" />
    </section>

    <section id="contacts" class="contacts fit q-mt-xl bg-light">
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
  },
  methods: {
    handleScroll(val) {
      this.$store.commit("bp/updHeaderTabValue", val);
      this.$router.push({ name: "home", hash: "#" + val });
    }
  }
};
</script>

<style lang="stylus">
.slide-up-enter-active
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1)

.slide-up-enter
  margin-top: 0
  transform: translateY(-7rem)

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
