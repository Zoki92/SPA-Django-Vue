import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/home/Home";
import IncidentDetail from "@/components/incident/IncidentDetail";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/incident/:id",
      name: "IncidentDetail",
      component: IncidentDetail
    }
  ]
});
