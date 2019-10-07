export function updDrawerState(state, value) {
  if (value === "left") {
    state.drawerLeft = !state.drawerLeft;
  } else if (value === "right") {
    state.drawerRight = !state.drawerRight;
  }
}
export function updHeaderTabValue(state, value) {
  state.tab = value;
}
