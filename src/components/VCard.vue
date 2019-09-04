<template>
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
</template>

<script>
export default {
  name: "VCard",
  data() {
    return {
      autoplay: true,
      slide: 1,
      slideTitle: "Пункт назначения",
      slideSubtitle: "Аннотация",
      images: [
        "https://cdn.quasar.dev/img/mountains.jpg",
        "https://cdn.quasar.dev/img/parallax1.jpg",
        "https://cdn.quasar.dev/img/parallax2.jpg"
      ],
      toursInfo: ["Первый маршрут", "Второй маршрут", "Третий маршрут"],
      tourDetail: null,
      expanded: false
    };
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
      this.autoplay = false;
      setTimeout(() => {
        this.expanded = true;
      }, 888);
    }
  }
};
</script>
