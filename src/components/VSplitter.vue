<template>
  <div>
    <q-resize-observer @resize="onResize" />
    <q-splitter
      v-model="splitterModel"
      :limits="[minPoint, maxPoint]"
      :horizontal="horizontal"
      style="height: 466px"
      before-class="q-ma-md overflow-hidden"
      separator-class="q-my-xl q-mx-lg"
      after-class="overflow-hidden"
    >
      <template v-slot:before>
        <div class="row">
          <q-list class="row-inline q-pa-md">
            <q-item>
              <q-item-section avatar>
                <q-icon color="primary" name="fas fa-map-marked-alt" />
              </q-item-section>
              <q-item-section>
                <span class="text-h6">Республика Казахстан, г.Павлодар,</span>
                <span class="text-h6"
                  >ул.Академика Сатпаева, д.65, офис 315.</span
                >
              </q-item-section>
            </q-item>

            <div class="row">
              <q-separator inset="item" spaced />
              <q-space class="col-auto q-ml-xl" />
            </div>

            <q-item>
              <q-item-section avatar>
                <q-icon color="primary" name="fas fa-phone-alt" />
              </q-item-section>
              <q-item-section>
                <span class="text-h6">+7(7182) 32-33-54</span>
              </q-item-section>
            </q-item>

            <div class="row">
              <q-separator inset="item" spaced />
              <q-space class="col-auto q-ml-xl" />
            </div>

            <q-item>
              <q-item-section avatar>
                <q-icon color="primary" name="fas fa-mobile-alt" />
              </q-item-section>
              <q-item-section>
                <span class="text-h6">+7(707) 462-66-69</span>
                <span class="text-h6">+7(705) 162-58-75</span>
              </q-item-section>
            </q-item>
          </q-list>
          <q-space />
        </div>
      </template>

      <template v-slot:separator>
        <q-avatar
          color="primary"
          text-color="white"
          size="2rem"
          :icon="avatarIcon"
        />
      </template>

      <template v-slot:after>
        <div class="map">
          <h4 class="map map__title text-center">Мы на карте</h4>
          <div>
            <YaMaps />
          </div>
        </div>
      </template>
    </q-splitter>
  </div>
</template>

<script>
import YaMaps from "components/YaMaps";
export default {
  name: "VSplitter",
  components: {
    YaMaps
  },
  data() {
    return {
      avatarIcon: "fas fa-arrows-alt-h",
      minPoint: 35,
      maxPoint: 100,
      horizontal: false,
      splitterModel: 50,
      stackColumns: false
    };
  },
  methods: {
    onResize({ width }) {
      if (width < 800) {
        this.avatarIcon = "fas fa-arrows-alt-v";
        this.horizontal = true;
        this.minPoint = 0;
        this.maxPoint = 94;
      } else {
        this.avatarIcon = "fas fa-arrows-alt-h";
        this.horizontal = false;
        this.minPoint = 35;
        this.maxPoint = 100;
      }
    }
  }
};
</script>

<style lang="stylus">
.map
  &__title
    margin: 1.09em 0
</style>
