export default {
  updDrawerState(state, value) {
    if (value === "l") {
      state.drawerLeft = !state.drawerLeft;
    } else if (value === "r") {
      state.drawerRight = !state.drawerRight;
    }
  },
  updHeaderTabValue(state, value) {
    state.tab = value;
  }
};
