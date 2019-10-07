const changeRoute = {
  methods: {
    changeTab(val) {
      this.$store.commit("bp/updHeaderTabValue", val);
    },
    changeRoute(routeName, routeHash = "") {
      console.log(this.$route.name);
      console.log(routeName);
      console.log(this.$route.hash);
      console.log(routeHash);
      if (this.$route.name === routeName && this.$route.hash === routeHash) {
        return;
      }

      let tab = routeName;
      let route = { name: routeName };

      if (routeHash) {
        route.hash = routeHash;
        tab = routeHash.split("#")[1];
        console.log(tab);
        console.log(route.hash);
      }

      this.$router.push(route);
      this.changeTab(tab);
    }
  }
};

export default changeRoute;
