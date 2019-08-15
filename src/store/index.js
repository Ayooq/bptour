/* eslint-disable no-undef */
import Vue from "vue";
import Vuex from "vuex";

// we first import the module
import bp from "./bp";

Vue.use(Vuex);

export default function(/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      // then we reference it
      bp
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV
  });

  /*
    if we want some HMR magic for it, we handle
    the hot update like below. Notice we guard this
    code with "process.env.DEV" -- so this doesn't
    get into our production build (and it shouldn't).
  */

  if (process.env.DEV && module.hot) {
    module.hot.accept(["./bp"], () => {
      const newBp = require("./bp").default;
      Store.hotUpdate({ modules: { bp: newBp } });
    });
  }

  return Store;
}
