<template>
  <yandex-map
    :settings="settings"
    :coords="coords1"
    ymap-class="ymap-body"
    zoom="17"
  >
    <ymap-marker
      :coords="coords2"
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
    settings: {
      apiKey: "affbda23-af60-4215-af8b-174a8101d71c",
      lang: "ru_RU",
      version: "2.1"
    },
    coords1: [52.283, 76.942],
    coords2: [52.2819, 76.942099],
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
.ymap-body
  >:nth-child(1)
    padding-top: 5rem

    >:nth-child(1)
      min-width: 1100px
      min-height: 300px
</style>
