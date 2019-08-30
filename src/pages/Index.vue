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
            class="shadow-24"
            height="500px"
            transition-next="jump-left"
            transition-prev="jump-right"
            arrows
            animated
            autoplay
            infinite
          >
            <q-carousel-slide
              v-scroll-to="'#details'"
              v-for="i in images.length"
              :key="i"
              :name="i"
              :img-src="images[i - 1]"
              @click="expandInfo(i - 2)"
            >
              <div id="details" class="tours tours__caption absolute-bottom">
                <div class="q-py-md text-h2">{{ slideTitle }}</div>
                <div class="q-py-md text-h6">{{ slideSubtitle }}</div>
              </div>
            </q-carousel-slide>
          </q-carousel>
        </q-card-section>

        <q-expansion-item>
          <q-card-section>
            <h4 class="tours tours__text q-pa-md">{{ toursInfo[slide] }}</h4>
          </q-card-section>
        </q-expansion-item>
      </q-card>
    </section>

    <section id="about" class="about row">
      <div id="about" class="hero hero__footer col-12 q-pa-md">
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam
        maiores fugit eum! Odio rem iste error cum distinctio, praesentium
        explicabo vitae ut, debitis officia sapiente ipsam, mollitia natus
        quidem reprehenderit! Lorem ipsum dolor sit amet consectetur adipisicing
        elit. A assumenda magni unde hic harum, consequuntur quae accusamus
        delectus, itaque sed animi deleniti distinctio esse dignissimos
        voluptas? Perferendis perspiciatis praesentium quod. Voluptas accusamus
        temporibus excepturi saepe ipsum rem quasi eos nulla cupiditate
        blanditiis deserunt possimus, laborum iure fugit repellat odio maxime
        soluta similique officia! Ipsa minus repellat quae quasi vel quis!
        Facere fuga pariatur tenetur distinctio, perspiciatis voluptatum veniam,
        accusamus fugit tempora eveniet inventore, id facilis saepe blanditiis
        ad. Officia impedit minima odio eos, similique maxime rerum nostrum
        excepturi laudantium? Assumenda? Optio voluptate iste possimus fugit
        omnis repellat non qui velit explicabo voluptatem aliquam veritatis
        dignissimos, facilis pariatur libero animi sunt reiciendis porro eius
        dolorem esse temporibus eaque! Eum, sit corrupti! Nihil, ipsa assumenda.
        In similique accusamus iste maiores rerum quidem, soluta, eius quibusdam
        molestias at excepturi sint adipisci, architecto earum voluptatibus?
        Excepturi neque quo accusantium veniam explicabo, maiores officia nulla.
        Esse culpa temporibus, tempore vel maiores eveniet debitis, nemo dolores
        ratione rem corrupti earum quibusdam iste ipsam officia voluptatem quia
        pariatur eligendi neque possimus? Minima nostrum incidunt odit non
        velit? Doloribus explicabo excepturi laboriosam officiis tenetur fugiat
        cum, dignissimos dicta reprehenderit ratione ipsam non maxime accusamus
        voluptatem harum tempora culpa facilis aliquid voluptatum doloremque.
        Facere quibusdam mollitia optio veniam et. Fugit nihil repellendus,
        pariatur eos accusantium, nemo et nam praesentium, amet repellat numquam
        saepe est neque? Placeat eum ullam assumenda non nostrum, culpa quos ex,
        veritatis laborum voluptatibus provident blanditiis. Reprehenderit,
        nesciunt amet, at fuga, modi adipisci ipsa tenetur quaerat dolorum nam
        ab id! Dignissimos illo doloremque nam omnis similique quas, iure earum
        est nobis corporis hic vero perspiciatis maxime. Natus molestiae fugit
        quaerat. Odit dolore perferendis ex sequi necessitatibus aperiam
        voluptatibus minus doloribus vitae, nesciunt natus tempore id quisquam
        libero iste est architecto sunt optio ducimus. Cupiditate,
        exercitationem iusto? Nihil odio itaque, atque fugit assumenda nemo,
        dolorem porro praesentium aliquid vero libero omnis provident
        dignissimos, eveniet eum ullam iusto quo distinctio esse vitae placeat
        inventore nisi obcaecati! Facere, laborum!
      </div>
    </section>

    <section id="contacts" class="footer row">
      <div class="col-12 q-ma-xl">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia,
        consequuntur, officia ipsa facere repellendus quibusdam, possimus maxime
        aut eaque sint error eveniet omnis sapiente ullam? Nulla quos
        praesentium ducimus soluta.
      </div>
    </section>
  </q-page>
</template>

<script>
export default {
  name: "PageIndex",
  data() {
    return {
      slide: 1,
      slideTitle: "Пункт назначения",
      slideSubtitle: "Аннотация",
      images: [
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg"
      ],
      toursInfo: ["Первый маршрут", "Второй маршрут", "Третий маршрут"],
      isVisible: false
    };
  },
  computed: {
    parallaxHeight() {
      return window.innerHeight;
    }
  },
  methods: {
    expandInfo(i) {
      console.log(i);
      this.tour = this.toursInfo[i];
      this.isVisible = true;
    }
  }
};
</script>

<style lang="stylus" scoped>
.bg-light
  background-color: $light
  color: $dark

.bg-dark
  background-color: $dark
  color: $light

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
    color: $dark
    text-align: justify

.my-card
  max-width: 250px
  width: 100%
</style>
