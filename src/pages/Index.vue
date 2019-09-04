<template>
  <q-page class="flex transparent no-scroll bg-light">
    <section id="home" class="hero full-width">
      <VParallax />
    </section>

    <section class="tours relative-position fit bg-dark">
      <VCard />
    </section>

    <section id="contacts" class="contacts fit bg-light">
      <div class="q-ma-xl">
        <h3 class="text-center">Контактная информация</h3>
        <q-splitter
          v-model="splitterModel"
          :limits="[35, 100]"
          :horizontal="stackColumns"
          after-class="overflow-hidden"
          style="height: 400px"
        >
          <template v-slot:before>
            <q-list class="row-inline q-mt-md">
              <q-item>
                <q-item-section avatar>
                  <q-icon color="primary" name="fas fa-map-marked-alt" />
                </q-item-section>
                <q-item-section>
                  <span class="text-h6">Республика Казахстан, г.Павлодар,</span>
                  <span class="text-h6"
                    >ул.Академика Сатпаева, д.65, офис 315.</span
                  >
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section avatar>
                  <q-icon color="primary" name="fas fa-phone-alt" />
                </q-item-section>
                <q-item-section>
                  <span class="text-h6 q-mr-xl">+7(7182) 32-33-54</span>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section avatar>
                  <q-icon color="primary" name="fas fa-mobile-alt" />
                </q-item-section>
                <q-item-section>
                  <span class="text-h6">+7(707) 462-66-69</span>
                  <span class="text-h6">+7(705) 162-58-75</span>
                </q-item-section>
              </q-item>
            </q-list>
          </template>

          <template v-slot:separator>
            <q-avatar
              color="primary"
              text-color="white"
              size="2rem"
              icon="fas fa-arrows-alt-h"
            />
          </template>

          <template v-slot:after>
            <div class="full-height q-pl-xl">
              <h4 class="map map__title text-center">Мы на карте</h4>
              <div class="fit q-ma-md">
                <YaMaps />
              </div>
            </div>
          </template>
        </q-splitter>
      </div>
    </section>
  </q-page>
</template>

<script>
import VParallax from "components/VParallax";
import VCard from "components/VCard";
import YaMaps from "components/YaMaps";

export default {
  name: "PageIndex",
  components: {
    VParallax,
    VCard,
    YaMaps
  },
  data() {
    return {
      splitterModel: 50,
      stackColumns: false
    };
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
    padding: 12px
    background-color: rgba(0, 0, 0, 0.3)

  &__text
    margin-top: -0.7em
    color: $dark
    text-align: justify

.map
  &__title
    margin: 1.3rem
</style>
