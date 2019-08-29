<template>
  <q-page class="index flex transparent no-scroll">
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

    <section id="tours" class="main window-width q-px-xl">
      <q-card class="card card__content q-my-xl q-py-xl">
        <div class="q-gutter-xl">
          <q-card-section>
            <q-item-label class="card card__label q-pa-xl inset-shadow text-h1"
              >Горящие туры</q-item-label
            >
            <q-carousel
              v-model="slide"
              class="card card_header col-12 shadow-24"
              height="500px"
              transition-next="jump-left"
              transition-prev="jump-right"
              arrows
              animated
              autoplay
              infinite
            >
              <q-carousel-slide
                name="first"
                img-src="https://cdn.quasar.dev/img/mountains.jpg"
                @click="showDetails"
              >
                <div class="card card__caption absolute-bottom">
                  <div class="text-h2">First stop</div>
                  <div class="text-subtitle1">Mountains</div>
                </div>
              </q-carousel-slide>
              <q-carousel-slide
                name="second"
                img-src="https://cdn.quasar.dev/img/parallax1.jpg"
              >
                <div class="card card__caption absolute-bottom">
                  <div class="text-h2">Second stop</div>
                  <div class="text-subtitle1">Famous City</div>
                </div>
              </q-carousel-slide>
              <q-carousel-slide
                name="third"
                img-src="https://cdn.quasar.dev/img/parallax2.jpg"
              >
                <div class="card card__caption absolute-bottom">
                  <div class="text-h2">Third stop</div>
                  <div class="text-subtitle1">Famous Bridge</div>
                </div>
              </q-carousel-slide>
            </q-carousel>
          </q-card-section>

          <q-card-section>
            <h4 class="card card__text">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse
              dignissimos non voluptatem, nihil voluptatum culpa cum corporis
              odio reprehenderit illo. Quo ducimus architecto mollitia minus
              maxime in, voluptates voluptate beatae?
            </h4>
          </q-card-section>
        </div>
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
      slide: "first"
    };
  },
  computed: {
    parallaxHeight() {
      return window.innerHeight;
    }
  },
  methods: {
    showDetails() {
      // this.$router
    }
  }
};
</script>

<style lang="stylus" scoped>
.index
  color: $dark

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

.main
  background-color: $blue-grey-10

.card
  color: $warning
  text-align: center

  &__content
    margin-top: -7rem
    background: radial-gradient(circle, $primary 0, $deep-orange-12 100%)

  &__label
    background-color: $deep-orange-10

  &__caption
    padding: 12px
    background-color: rgba(0, 0, 0, 0.3)

  &__text
    color: $dark
    text-align: justify
</style>
