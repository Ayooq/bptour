<template>
  <q-card class="tours tours__content tours__content_bg q-pt-xl shadow-5">
    <q-card-section>
      <q-item-label
        id="tours"
        class="tours tours__label-bg q-py-md inset-shadow"
      >
        <span class="tours tours__label-header">Основные направления</span>
      </q-item-label>
      <q-carousel
        v-model="slide"
        :autoplay="autoplay"
        id="details"
        class="shadow-24"
        height="30rem"
        transition-next="jump-left"
        transition-prev="jump-right"
        navigation-icon="fas fa-circle text-warning"
        navigation
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
          <div class="tours tours__caption absolute-bottom text-h3">
            {{ slideTitle }}
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
      images: [
        "statics/images/beach1.jpg",
        "statics/images/maldives1.jpg",
        "statics/images/oia.jpg",
        "statics/images/temple.jpg",
        "statics/images/schilthorn.jpg"
      ],
      toursInfo: [
        "Развёрнутое описание 1",
        "Развёрнутое описание 2",
        "Развёрнутое описание 3",
        "Развёрнутое описание 4",
        "Развёрнутое описание 5"
      ],
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
      this.$store.commit("bp/updHeaderTabValue", "tours");
      setTimeout(() => {
        this.expanded = true;
      }, 888);
    }
  }
};
</script>
