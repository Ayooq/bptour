<template>
  <q-page class="flex transparent">
    <section id="home" class="hero full-width">
      <q-parallax :height="parallaxHeight">
        <template v-slot:media>
          <img src="statics/images/beach3.jpg" />
        </template>

        <template v-slot:content="scope">
          <div
            class="row items-end justify-center"
            :style="{
              opacity: 0.82 + (0.6 - scope.percentScrolled) * 0.92
            }"
          >
            <img
              class="hero hero__logo col-md-3 q-mb-sm"
              src="assets/bp-logo-full.svg"
            />
            <div class="col-md-9 col-auto column items-center">
              <span class="hero hero__subtitle gt-xs text-h6 q-pl-xl q-ml-xl"
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

    <section id="tours" class="main full-width q-px-xl">
      <q-card class="main main__content q-my-xl q-py-xl" bordered>
        <div class="q-gutter-xl">
          <q-card-section>
            <q-item-label class="text-h1 text-center text-deep-orange-12"
              >Горящие туры</q-item-label
            >
          </q-card-section>

          <q-card-section>
            <q-carousel
              v-model="slide"
              class="main main_header col-12"
              height="500px"
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
                <div class="absolute-bottom custom-caption">
                  <div class="text-h2">First stop</div>
                  <div class="text-subtitle1">Mountains</div>
                </div>
              </q-carousel-slide>
              <q-carousel-slide
                name="second"
                img-src="https://cdn.quasar.dev/img/parallax1.jpg"
              >
                <div class="absolute-bottom custom-caption">
                  <div class="text-h2">Second stop</div>
                  <div class="text-subtitle1">Famous City</div>
                </div>
              </q-carousel-slide>
              <q-carousel-slide
                name="third"
                img-src="https://cdn.quasar.dev/img/parallax2.jpg"
              >
                <div class="absolute-bottom custom-caption">
                  <div class="text-h2">Third stop</div>
                  <div class="text-subtitle1">Famous Bridge</div>
                </div>
              </q-carousel-slide>
            </q-carousel>
          </q-card-section>

          <q-card-section>
            <div>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse
              dignissimos non voluptatem, nihil voluptatum culpa cum corporis
              odio reprehenderit illo. Quo ducimus architecto mollitia minus
              maxime in, voluptates voluptate beatae?
            </div>
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
      <div class="col-12 q-pa-md">
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
.hero
  color: $light

  &__logo
    max-width: 12rem
    max-height: 12rem

  &__subtitle
    margin-bottom: -17px

  &__cta
    background-color: $primary
    color: $dark
    font-size: 1.3em

.main
  background-color: $blue-grey-10

  &__content
    margin-top: -7rem
    background-color: #b5fdff

.custom-caption
  padding: 12px
  background-color: rgba(0, 0, 0, 0.3)
  color: white
  text-align: center
</style>
