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
        <q-flashcard-section :transition="transitions[10]">
          <img :src="item" />
        </q-flashcard-section>
        <q-flashcard-section :transition="transitions[0]" class="fit">
          <div class="fit" style="background-color: rgba(219,127,8, 0.3);" />
          <q-flashcard-section
            :transition="transitions[34]"
            class="q-pa-xl text-h5 text-info"
          >
            For beautiful eyes, look for the good in others; for beautiful lips,
            speak only words of kindness; and for poise, walk with the knowledge
            that you are never alone.
          </q-flashcard-section>
          <q-flashcard-section
            :transition="transitions[27]"
            class="fit flex justify-center items-center q-pt-xl"
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
      ],
      transitions: [
        "fade-in",
        "fade-out",
        "flip-left-in",
        "flip-left-out",
        "flip-right-in",
        "flip-right-out",
        "flip-down-in",
        "flip-down-out",
        "flip-up-in",
        "flip-up-out",
        "nudge-in",
        "nudge-out",
        "roll-left-in",
        "roll-right-in",
        "roll-down-in",
        "roll-up-up",
        "roll-left-out",
        "roll-right-out",
        "roll-down-out",
        "roll-up-out",
        "shake-left",
        "shake-right",
        "shake-down",
        "shake-up",
        "slide-left-in",
        "slide-right-in",
        "slide-down-in",
        "slide-up-in",
        "slide-left-out",
        "slide-right-out",
        "slide-down-out",
        "slide-up-out",
        "spin-in",
        "spin-out",
        "zoom-in",
        "zoom-out"
      ]
    };
  },
  computed: {
    style() {
      return {
        minWidth: "450px",
        minHeight: "450px",
        borderRadius: "8rem",
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

<style lang="stylus">
.f-card
  text-align: center
  text-shadow: 1px 1px 1px $dark

  &__btn
    background: $info
    color: $light
</style>
