<template>
  <yandex-map :settings="settings" :coords="coords" zoom="17">
    <ymap-marker
      :coords="coords"
      :icon="markerIcon"
      ymap-class="map ymap-body"
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
    settings: {
      apiKey: "affbda23-af60-4215-af8b-174a8101d71c",
      lang: "ru_RU",
      version: "2.1"
    },
    coords: [52.281892, 76.942061],
    markerIcon: {
      color: "orange",
      content: "Мы здесь!"
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
    min-width: 1000px
    min-height: 25.5rem

    @media (max-width: $breakpoint-sm-max)
      min-width: 300px
</style>
