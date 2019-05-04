// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App";
import router from "./router";
import fontawesome from "@fortawesome/fontawesome";
import regular from "@fortawesome/fontawesome-free-regular";
import solid from "@fortawesome/fontawesome-free-solid";
import store from "./store";
import VueNativeSock from "vue-native-websocket";
import axios from "axios";

fontawesome.library.add(regular);
fontawesome.library.add(solid);
Vue.config.productionTip = false;

if (process.env.NODE_ENV === "development") {
  (axios.defaults.baseURL = "http://localhost:8000/"),
    (Vue.prototype.webSocketBaseURL = "ws://localhost:8000/ws/");
} else {
  // production settings
}
Vue.use(VueNativeSock, Vue.prototype.webSocketBaseURL, {
  store: store,
  reconnection: true,
  reconnectionDelay: 3000
});

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>"
});
