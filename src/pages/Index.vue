<template>
  <q-page class="flex transparent">
    <section class="hero row">
      <q-parallax class="hero hero__header col-12" :height="parallaxHeight">
        <template v-slot:media>
          <img src="statics/images/beach3.jpg" />
        </template>

        <template v-slot:content="scope">
          <div
            class="absolute column items-center"
            :style="{
              opacity: 0.69 + (1 - scope.percentScrolled) * 0.55,
              top: scope.percentScrolled * 30 + '%'
            }"
          >
            <img
              src="assets/bp-logo-full.svg"
              style="width: 150px; height: 150px"
            />
            <div class="text-h3 text-white text-center">Бюро Путешествий</div>
            <div class="text-h6 text-grey-3 text-center">Тур-агентство</div>
          </div>
        </template>
      </q-parallax>
      <div class="hero hero__footer col-12 q-pa-md">
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
    <section class="main row window-height">
      <q-carousel
        v-model="slide"
        class="main main_header col-12"
        height="400px"
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
      <div class="col-12 q-pa-md">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio
        asperiores placeat eligendi iure. Unde assumenda velit exercitationem,
        provident dolor culpa veniam laborum libero, qui illo dolore eos in
        optio sit! Placeat, saepe eius! Maiores provident architecto quis
        facilis odit officia placeat sit voluptates accusantium temporibus odio
        deserunt tempore earum aliquid ut, quibusdam modi id soluta aut dolore
        obcaecati. Impedit, ut. Animi quasi iste at in reprehenderit ullam
        ducimus dolore expedita excepturi, natus, esse aspernatur similique,
        accusantium atque! Nemo, iure excepturi aliquam esse illo, veniam,
        quibusdam consequuntur rerum error alias optio. Harum iste nisi maxime
        possimus ullam dolorum esse repudiandae accusamus excepturi voluptatem
        in expedita, quisquam quod ratione, laborum voluptatum repellendus nobis
        praesentium cupiditate reprehenderit consequuntur sequi, voluptas
        aliquam atque! Esse. Cupiditate veritatis ut harum placeat aut fugit
        pariatur voluptatibus sunt quam vel. Blanditiis velit accusantium ea,
        ratione, suscipit temporibus corporis excepturi magnam non delectus,
        modi nulla sed neque numquam dolorem. Voluptatem nesciunt exercitationem
        delectus qui nisi assumenda animi ea consequuntur veniam quos dolor,
        magni eos adipisci omnis facilis molestiae illum architecto eveniet.
        Officia culpa, nesciunt non natus suscipit deserunt incidunt.
      </div>
    </section>
    <section class="footer row">
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
      parallaxHeight: window.innerHeight / 1.33,
      slide: "first"
    };
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
  &__footer
    font-family: serif

.custom-caption
  padding: 12px
  background-color: rgba(0, 0, 0, 0.3)
  color: white
  text-align: center
</style>
