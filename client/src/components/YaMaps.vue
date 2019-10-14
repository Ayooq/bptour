<template>
  <yandex-map :settings="settings" :coords="coords" zoom="17">
    <ymap-marker
      :coords="coords"
      :icon="markerIcon"
      marker-id="123"
      hint-content="Бюро Путешествий"
    />
  </yandex-map>
</template>

<script>
import { yandexMap, ymapMarker } from "vue-yandex-maps";

export default {
  name: "YaMaps",
  components: {
    yandexMap,
    ymapMarker
  },
  data: () => ({
    coords: [52.281892, 76.942061],
    markerIcon: {
      color: "orange",
      content: "Мы здесь!"
    },
    settings: {
      apiKey: "affbda23-af60-4215-af8b-174a8101d71c",
      lang: "ru_RU",
      version: "2.1"
    }
  }),
  methods: {
    onClick(e) {
      this.coords = e.get("coords");
    }
  }
};
</script>

<style lang="stylus">
.ymap-container
  >:nth-child(1)
    min-height: 24rem
</style>
