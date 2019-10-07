<template>
  <q-card class="no-shadow">
    <q-parallax src="statics/images/maldives2.jpg" :height="300" />

    <q-card-section>
      <div class="text-h6 text-secondary">Our Changing Planet</div>
      <div class="text-subtitle2 text-secondary">by John Doe</div>
    </q-card-section>

    <q-tabs v-model="tab" class="text-info">
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
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
        <p>
          The QCard component is a great way to display important pieces of
          grouped content.
        </p>
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

<style lang="stylus" scoped></style>
