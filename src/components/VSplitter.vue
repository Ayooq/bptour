<template>
  <div>
    <q-resize-observer @resize="onResize" />
    <q-splitter
      v-model="splitterModel"
      :limits="[minPoint, maxPoint]"
      :horizontal="horizontal"
      style="height: 400px"
      before-class="q-pa-md overflow-hidden"
      after-class="overflow-hidden"
    >
      <template v-slot:before>
        <q-list class="row-inline q-mt-md">
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
          <q-item>
            <q-item-section avatar>
              <q-icon color="primary" name="fas fa-phone-alt" />
            </q-item-section>
            <q-item-section>
              <span class="text-h6 q-mr-xl">+7(7182) 32-33-54</span>
            </q-item-section>
          </q-item>
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
      </template>

      <template v-slot:separator>
        <q-avatar
          color="primary"
          text-color="white"
          size="2rem"
          icon="fas fa-arrows-alt-h"
        />
      </template>

      <template v-slot:after>
        <div class="map full-height q-pl-xl">
          <h4 class="map map__title text-center">Мы на карте</h4>
          <div class="fit q-ma-md">
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
      minPoint: 35,
      maxPoint: 100,
      horizontal: false,
      splitterModel: 50,
      stackColumns: false
    };
  },
  methods: {
    // we are using QResizeObserver to keep
    // this example mobile-friendly
    onResize({ width }) {
      if (width < 800) {
        this.horizontal = true;
        this.minPoint = 0;
      } else {
        this.horizontal = false;
        this.minPoint = 35;
      }
    }
  }
};
</script>

<style lang="stylus">
.map
  &__title
    margin: 1.3rem 0
</style>
