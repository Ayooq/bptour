<template>
  <q-page class="flex transparent no-scroll bg-light">
    <section id="home" class="hero full-width">
      <q-parallax :height="parallaxHeight">
        <template #media>
          <img src="statics/images/beach3.jpg" />
        </template>

        <template #content="scope">
          <div
            class="absolute row justify-center items-center q-pa-lg"
            :style="{
              opacity: 0.82 + (0.6 - scope.percentScrolled) * 0.92,
              left: 0,
              top: 0,
              right: 0,
              bottom: scope.percentScrolled * 50 + '%'
            }"
          >
            <img
              class="hero hero__logo col-md-6 q-my-sm"
              src="assets/bp-logo-full.svg"
            />
            <div class="col-md-auto column items-center">
              <span
                class="hero hero__subtitle gt-xs q-ml-xl q-mt-lg q-pl-xl text-h6"
                >Тур-агентство</span
              >
              <p class="hero hero__title text-h3 text-center">
                Бюро Путешествий
              </p>
              <q-btn
                v-scroll-to="'#tours'"
                class="hero hero__cta q-mb-sm"
                label="Начать путешествие"
                glossy
                push
                rounded
                unelevated
              />
            </div>
          </div>
        </template>
      </q-parallax>
    </section>

    <section class="tours relative-position fit bg-dark">
      <q-card class="tours tours__content tours__content_bg q-pt-xl shadow-5">
        <q-card-section>
          <q-item-label
            id="tours"
            class="tours tours__label q-pa-xl inset-shadow text-h1"
            >Горящие туры</q-item-label
          >
          <q-carousel
            v-model="slide"
            :autoplay="autoplay"
            id="details"
            class="shadow-24"
            height="500px"
            transition-next="jump-left"
            transition-prev="jump-right"
            arrows
            animated
            infinite
            padding
            swipeable
            @input="updateTourDetails"
          >
            <q-carousel-slide
              v-scroll-to="'#details'"
              v-for="(item, index) in images"
              :key="index"
              :name="index"
              :img-src="item"
              @click="expandInfo"
            >
              <div class="tours tours__caption absolute-bottom">
                <div class="q-py-md text-h2">{{ slideTitle }}</div>
                <div class="q-py-md text-h6">{{ slideSubtitle }}</div>
              </div>
            </q-carousel-slide>
          </q-carousel>
        </q-card-section>

        <q-expansion-item
          v-model="expanded"
          expand-icon-class="invisible"
          expand-icon-toggle
          @show="showTourDetails"
        >
          <q-card-section>
            <h4 class="tours tours__text q-px-md">{{ tourDetail }}</h4>
          </q-card-section>
        </q-expansion-item>
      </q-card>
    </section>

    <section id="contacts" class="contacts fit bg-light">
      <div class="q-ma-xl">
        <h3 class="text-center">Наши контакты</h3>
        <q-splitter
          v-model="splitterModel"
          :limits="[42, 100]"
          :horizontal="stackColumns"
          after-class="overflow-hidden"
          style="height: 400px"
        >
          <template v-slot:before>
            <q-list class="row q-mt-md">
              <q-item class="col-12 row justify-start">
                <q-item-section class="col-auto" avatar>
                  <q-icon color="primary" name="fas fa-map-marked-alt" />
                </q-item-section>
                <q-item-section class="col">
                  <span class="text-h6">
                    Республика Казахстан, город Павлодар, ул.Академика Сатпаева,
                    д.65, офис 315.
                  </span>
                </q-item-section>
              </q-item>
              <q-item class="col row-inline justify-start">
                <q-item-section class="col-auto" avatar>
                  <q-icon color="primary" name="fas fa-phone-alt" />
                </q-item-section>
                <q-item-section class="col-auto">
                  <span class="text-h6 q-mr-xl">8(7182)32-33-54</span>
                </q-item-section>
                <q-item-section class="on-left" avatar>
                  <q-icon color="primary" name="fas fa-mobile-alt" />
                </q-item-section>
                <q-item-section class="col-auto">
                  <span class="text-h6">+7(707)462-66-69</span>
                  <span class="text-h6">+7(705)162-58-75</span>
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
            <div class="q-pa-md">
              <div class="text-h4 q-mb-md">Карта</div>
              <div v-for="n in 20" :key="n" class="q-my-md">
                {{ n }}. Lorem ipsum dolor sit, amet consectetur adipisicing
                elit. Quis praesentium cumque magnam odio iure quidem, quod
                illum numquam possimus obcaecati commodi minima assumenda
                consectetur culpa fuga nulla ullam. In, libero.
              </div>
            </div>
          </template>
        </q-splitter>
      </div>
    </section>
  </q-page>
</template>

<script>
export default {
  name: "PageIndex",
  data() {
    return {
      autoplay: true,
      slide: 1,
      slideTitle: "Пункт назначения",
      slideSubtitle: "Аннотация",
      images: Array(
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg"
      ),
      toursInfo: ["Первый маршрут", "Второй маршрут", "Третий маршрут"],
      tourDetail: null,
      expanded: false,
      splitterModel: 42,
      stackColumns: false
    };
  },
  computed: {
    parallaxHeight() {
      return window.innerHeight;
    }
  },
  methods: {
    showTourDetails() {
      this.tourDetail = this.toursInfo[this.slide];
    },
    updateTourDetails() {
      if (this.expanded) {
        this.showTourDetails();
      }
    },
    expandInfo() {
      this.expanded = true;
      this.autoplay = false;
    }
  }
};
</script>

<style lang="stylus" scoped>
.hero
  color: $light

  &__logo
    max-width: 14rem
    max-height: 14rem

  &__subtitle
    margin-bottom: -17px

  &__cta
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
</style>
