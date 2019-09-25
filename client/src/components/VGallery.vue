<template>
  <div class="tours tours__gallery row q-py-xl q-px-md q-mb-xl justify-evenly">
    <h2 class="col-12 text-info q-pb-lg q-mx-sm">Другие направления</h2>
    <div
      v-for="(item, index) in images"
      :key="index"
      :name="index"
      class="porthole col-lg-3 col-md-4 col-sm-7 col-12 row q-ma-lg"
    >
      <q-flashcard :style="style" class="f-card col-auto q-ma-md">
        <q-flashcard-section transition="nudge-in">
          <img :src="item" class="f-card f-card__img" alt="img" />
        </q-flashcard-section>
        <q-flashcard-section transition="fade-out" class="fit">
          <div class="fit" style="background-color: rgba(219,127,8, 0.2);" />
          <q-flashcard-section
            transition="zoom-out"
            class="q-pa-xl text-h5 text-info"
          >
            <p class="q-ma-md q-py-md">
              For beautiful eyes, look for the good in others; for beautiful
              lips, speak only words of kindness; and for poise, walk with the
              knowledge that you are never alone.
            </p>
          </q-flashcard-section>
        </q-flashcard-section>
        <q-flashcard-section
          transition="zoom-in"
          class="flex fit justify-center items-center"
        >
          <q-btn
            v-scroll-to="'#contacts'"
            class="f-card f-card__btn"
            size="xl"
            push
            glossy
            rounded
            @click="changeTab('contacts')"
            >Заказать тур</q-btn
          >
        </q-flashcard-section>
      </q-flashcard>
    </div>
  </div>
</template>

<script>
export default {
  name: "VGallery",
  data() {
    return {
      images: [
        "statics/images/boat-house.jpg",
        "statics/images/louvre.jpg",
        "statics/images/maldives2.jpg",
        "statics/images/polynesia.jpg",
        "statics/images/schilthorn.jpg"
      ]
    };
  },
  computed: {
    style() {
      return {
        width: "500px",
        height: "500px",
        minWidth: 0,
        borderRadius: "50%"
      };
    },
    tab: {
      get() {
        return this.$store.state.bp.tab;
      },
      set(val) {
        this.$store.commit("bp/updHeaderTabValue", val);
      }
    }
  },
  methods: {
    changeTab(val) {
      this.tab = val;
    }
  }
};
</script>

<style lang="stylus">
.porthole
  border: 10px solid $info
  border-radius: 50%
  background: rgba(20, 174, 205, 0.8)
  opacity: 0.9

.f-card
  text-align: center
  text-shadow: 1px 1px 1px $dark

  &__img
    width: 500px
    height: 500px

  &__btn
    background: $info
    color: $light
</style>
