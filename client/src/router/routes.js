import AppLayout from "layouts/AppLayout.vue";
import HomePage from "pages/Index.vue";
import CountriesPage from "pages/Countries.vue";
import ErrorPage from "pages/Error404.vue";

const routes = [
  {
    path: "/",
    component: AppLayout,
    children: [
      { path: "", name: "home", component: HomePage },
      {
        path: "countries",
        name: "countries",
        component: CountriesPage
      }
    ]
  }
];

// Always leave this as last one
if (process.env.MODE !== "ssr") {
  routes.push({
    path: "*",
    component: ErrorPage
  });
}

export default routes;
