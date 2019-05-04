import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);
const debug = process.env.NODE_ENV !== "production";

export default new Vuex.Store({
  strict: debug,
  state: {
    socket: {
      isConnected: false,
      message: "",
      reconnectError: false
    },
    notificationErrors: [],
    sites: [],
    incidents: []
  },
  mutations: {
    SOCKET_ONOPEN(state, event) {
      console.log("What can I do for you?");
      state.socket.isConnected = true;
      state.notificationErrors.push({
        color: "green",
        id: 0,
        text: "We are connected now! This works great!",
        time: 0
      });
    },
    SOCKET_ONCLOSE(state, event) {
      console.log("Oh dang, I can't reach you anymore!");
      state.socket.isConnected = false;
      state.notificationErrors = state.notificationErrors.filter(
        a => a.id !== 0
      );
      if (state.notificationErrors.find(a => a.id === 0) === undefined) {
        state.notificationErrors.push({
          color: "red",
          id: 0,
          text:
            "We lost connection to the server. Please refresh the page or wait for a bit.",
          time: 0
        });
      }
    },
    SOCKET_ONERROR(state, event) {
      console.error(state, event);
    },
    // default handler called for all methods
    SOCKET_ONMESSAGE(state, message) {
      var data = JSON.parse(message.data)["message"];
      var i = state.sites.findIndex(o => o.id == data["id"]);
      state.sites[i] ? state.sites.splice(i, 1, data) : state.sites.push(data);
      var result = state.sites.map(a => a.incident_set);
      state.incidents = [].concat.apply([], result);
      state.socket.message = message;
    },
    // mutations for reconnect methods
    SOCKET_RECONNECT(state, count) {
      console.info(state, count);
    },
    SOCKET_RECONNECT_ERROR(state) {
      console.log("we are back up and sailing guys! Nothing to worry about.");
      state.socket.reconnectError = true;
    },
    addNotificationError(state, error) {
      error.id = btoa(Math.random()).substr(5, 5);
      state.notificationErrors.push(error);
    },
    removeNotificationError(state, error) {
      state.notificationErrors = state.notificationErrors.filter(
        a => a.id != error.id
      );
    }
  },
  actions: {
    showNotificationErrors({ commit }, error) {
      commit("addNotificationError", error);
      if (error.time) {
        setTimeout(() => {
          commit("removeNotificationError", error);
        }, error.time);
      }
    }
  }
});
