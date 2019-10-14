<template>
  <q-card class="no-shadow">
    <q-parallax :src="image" :height="300" />

    <q-card-section>
      <div class="text-h6 text-secondary">{{ countryName }}</div>
    </q-card-section>

    <q-tabs v-model="tab" class="text-info">
      <q-tab label="Tab one" name="one" />
      <q-tab label="Tab two" name="two" />
    </q-tabs>

    <q-separator />

    <q-tab-panels v-model="tab" animated>
      <q-tab-panel name="one">
        <p>{{ description }}</p>
      </q-tab-panel>

      <q-tab-panel name="two">
        <p>{{ additional }}</p>
      </q-tab-panel>
    </q-tab-panels>
  </q-card>
</template>

<script>
export default {
  name: "VDetailsCard",
  data() {
    return {
      image: "statics/images/maldives2.jpg",
      countryName: "Название страны",
      description: "Развёрнутое описание",
      additional: "Дополнительная информация",
      tab: "one"
    };
  },
  created() {
    this.$axios
      .get("/api/v2/pages/3/")
      .then(response => {
        console.log(response);
        // this.image = response.data.image;
        // this.countryName = response.data.country.name;
        // this.description = response.data.description;
        // this.additional = response.data.additional;
      })
      .catch(() => {
        this.$q.notify({
          color: "negative",
          position: "top",
          message: "Запрос к бэкэнду не удался",
          icon: "report_problem"
        });
      });
  }
};
</script>

<style lang="stylus" scoped></style>
