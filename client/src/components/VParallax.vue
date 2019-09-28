<template>
  <q-parallax :height="parallaxHeight">
    <template #media>
      <img src="statics/images/bora-bora.jpg" />
    </template>

    <template #content="scope">
      <div
        class="absolute row justify-center items-center content-center"
        :style="{
          opacity: 0.82 + (0.6 - scope.percentScrolled) * 0.92,
          top: 0,
          right: 0,
          bottom: scope.percentScrolled * 50 + '%',
          left: 0
        }"
      >
        <img
          class="hero hero__logo col-auto q-pb-lg"
          src="../assets/bp-logo-full.svg"
        />
        <div class="col-auto column items-center">
          <span class="hero hero__subtitle text-h6">Тур-агентство</span>
          <p class="text-h3 text-center">Бюро Путешествий</p>
          <q-btn
            v-scroll-to="'#tours'"
            class="hero hero__cta q-mb-sm bg-light"
            label="Отправиться в путешествие"
            glossy
            push
            rounded
            unelevated
            @click="$store.commit('bp/updHeaderTabValue', 'tours')"
          />
        </div>
      </div>
    </template>
  </q-parallax>
</template>

<script>
export default {
  name: "VParallax",
  computed: {
    parallaxHeight() {
      return window.innerHeight;
    }
  }
};
</script>
