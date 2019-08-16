import vueScrollTo from "vue-scrollto";

export default async ({ Vue }) => {
  Vue.use(vueScrollTo, {
    container: "body",
    duration: 1500,
    easing: "ease",
    offset: -100,
    force: true,
    cancelable: true,
    onStart: false,
    onDone: false,
    onCancel: false,
    x: false,
    y: true
  });
};
