<template>
  <div>
    <div :class="'indicator ' + status"></div>
    <p v-if="showText">{{message}}</p>
  </div>
</template>

<script>
export default {
  name: "IndicatorIcon",
  props: {
    status: {
      type: String,
      validator: function(value) {
        return ["up", "down", "issue"].indexOf(value) !== -1;
      }
    },
    showText: Boolean
  },
  computed: {
    message: function() {
      if (this.status === "up") {
        return "All is good";
      } else if (this.status === "down") {
        return "We are having issues";
      } else if (this.status === "issue") {
        return "You might notice some inconvenience";
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.indicator {
  height: 17px;
  width: 17px;
  border-radius: 50%;
  display: inline-block;
}
p {
  display: inline-block;
  position: relative;
  top: -3px;
  margin-left: 5px;
  font-size: 14px;
  color: #464646;
}
</style>
