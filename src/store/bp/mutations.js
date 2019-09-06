export function updDrawerState(state, value) {
  if (value === "l") {
    state.drawerLeft = !state.drawerLeft;
  } else if (value === "r") {
    state.drawerRight = !state.drawerRight;
  }
}
export function updHeaderTabValue(state, value) {
  state.tab = value;
}
