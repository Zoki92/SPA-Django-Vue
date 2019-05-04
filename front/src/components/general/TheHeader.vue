<template>
  <header>
    <div class="full-background">
      <div class="inner">
        <div class="upper">
          <img src="/static/images/logo.svg" class="image">
          <IndicatorIcon class="rightfloat" :status="status" :showText="true"/>
        </div>
        <div class="subscribe" v-show="showForm">
          Sign up to be notified of updates
          <div class="form">
            <input type="text" class="input-field" v-model="email">
            <button @click="sendEmail" class="subscribe-button">Subscribe</button>
          </div>
        </div>
        <div class="subscribe hover" @click="showForm = !showForm">Subscribe</div>
      </div>
    </div>
  </header>
</template>

<script>
import IndicatorIcon from "./IndicatorIcon.vue";
import axios from "axios";

export default {
  name: "TheHeader",
  components: { IndicatorIcon },
  data() {
    return {
      showForm: false,
      email: ""
    };
  },
  computed: {
    status: function() {
      if (
        this.$store.state.sites.find(a => a.status === "down") !== undefined
      ) {
        return "down";
      } else if (
        this.$store.state.sites.find(a => a.status === "issue") !== undefined
      ) {
        return "issue";
      } else {
        return "up";
      }
    }
  },
  methods: {
    sendEmail() {
      axios
        .post("api/subscribe", { email: this.email })
        .then(response => {
          this.$store.dispatch("showNotificationErrors", {
            color: "green",
            text: "Cool! We will notify you of incidents!",
            time: 2000
          });
          this.email = "";
          this.showForm = !this.showForm;
        })
        .catch(error => {
          if ("email" in error.response.data) {
            this.$store.dispatch("showNotificationErrors", {
              color: "red",
              text: error.response.data["email"][0],
              time: 2000
            });
          }
        });
    }
  }
};
</script>
<style scoped>
.full-background {
  padding-bottom: 80px;
  background-color: #6072b5;
}
.inner {
  margin: 0 auto 50px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  background-color: white;
  box-shadow: 0 0 3px 1px rgba(163, 163, 163, 0.3);
  -webkit-box-shadow: 0 0 3px 1px rgba(163, 163, 163, 0.3);
  max-width: 700px;
}
.image {
  margin: 10px 30px;
}
.rightfloat {
  float: right;
  margin-top: 13px;
  margin-right: 26px;
}
.upper {
  -webkit-box-shadow: 0px -1px 9px #636363;
  -moz-box-shadow: 0px -1px 9px #636363;
  box-shadow: 0px -1px 9px #636363;
}
.subscribe {
  text-align: center;
  border-bottom-left-radius: 8px;
  background-color: rgba(232, 232, 232, 0.6);
  border-bottom-right-radius: 8px;
  font-size: 12px;
  padding: 7px;
  color: rgba(49, 49, 72, 00.64);
  z-index: -1;
}
.hover:hover {
  background-color: rgba(232, 232, 232, 0.8);
  cursor: pointer;
}
.input-field {
  padding: 5px;
  width: 160px;
}
button:focus,
.input-field:focus {
  outline: 0;
}
.form {
  margin-top: 7px;
}
.subscribe-button {
  padding: 5px 10px 7px;
  border: 0px;
  background-color: #6072b5;
  color: white;
  top: -1px;
  position: relative;
}
.subscribe-button:hover {
  background-color: #48578c;
  cursor: pointer;
}
@media only screen and (max-width: 750px) {
  .inner {
    width: 100%;
  }
}
</style>
