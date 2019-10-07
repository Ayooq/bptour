<template>
  <div class="q-pa-md">
    <q-card class="my-card">
      <q-parallax src="statics/images/maldives1.jpg" :height="300" />

      <q-card-section>
        <div class="text-h6">Our Changing Planet</div>
        <div class="text-subtitle2">by John Doe</div>
      </q-card-section>

      <q-tabs v-model="tab" class="text-teal">
        <q-tab label="Tab one" name="one" />
        <q-tab label="Tab two" name="two" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="one">
          <p>
            The QCard component is a great way to display important pieces of
            grouped content.
          </p>
        </q-tab-panel>

        <q-tab-panel name="two">
          <p>
            With so much content to display at once, and often so little screen
            real-estate, Cards have fast become the design pattern of choice for
            many companies, including the likes of Google and Twitter.
          </p>
        </q-tab-panel>
      </q-tab-panels>
    </q-card>
  </div>
</template>

<script>
export default {
  name: "VDetailsCard",
  data() {
    return {
      tab: "one"
    };
  }
};
</script>

<style lang="stylus" scoped>
.my-card
  min-width: 250px
  width: 100%
</style>
