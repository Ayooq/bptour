<template>
  <div class="q-px-xl q-pb-xl">
    <h1 class="text-info q-pb-lg">Другие направления</h1>
    <div class="row q-gutter-xl">
      <q-flashcard
        v-for="(item, index) in images"
        :key="index"
        :name="index"
        :style="style"
        class="col"
      >
        <q-flashcard-section transition="nudge-in">
          <img :src="item" />
        </q-flashcard-section>
        <q-flashcard-section transition="fade-in" class="fit">
          <div class="fit" style="background-color: rgba(219,127,8, 0.3);" />
          <q-flashcard-section
            transition="slide-up-in"
            class="q-pa-xl text-h5 text-info"
          >
            For beautiful eyes, look for the good in others; for beautiful lips,
            speak only words of kindness; and for poise, walk with the knowledge
            that you are never alone.
          </q-flashcard-section>
          <q-flashcard-section
            transition="fade-in"
            class="fit flex justify-center items-center q-pt-xl"
          >
            <q-btn
              v-scroll-to="'#contacts'"
              class="bg-info"
              size="xl"
              push
              glossy
              rounded
              @click="changeTab('contacts')"
              >Заказать тур</q-btn
            >
          </q-flashcard-section>
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
        "statics/images/beach2.jpg",
        "statics/images/beach3.jpg",
        "statics/images/maldives2.jpg",
        "statics/images/bora-bora.jpg",
        "statics/images/louvre.jpg",
        "statics/images/schilthorn.jpg"
      ]
    };
  },
  computed: {
    style() {
      return {
        minHeight: "450px",
        minWidth: "450px",
        textAlign: "center",
        boxShadow: "1px 1px 2px #e6e6e6"
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

<style></style>
