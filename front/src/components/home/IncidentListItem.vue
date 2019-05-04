<template>
  <div>
    <h2>{{ incident.title }}</h2>
    <p>{{ lastUpdate.description }}</p>
    <div class="half">{{lastUpdate.date | timeAgo}}</div>
    <div class="half right">Status: {{lastUpdate.status}}</div>
  </div>
</template>
<script>
import { timeFormatter } from "@/mixins/DateTimeFilters";
export default {
  name: "Incident",
  mixins: [timeFormatter],
  props: {
    incident: Object
  },
  computed: {
    lastUpdate: function() {
      return this.incident.update_set[0];
    }
  }
};
</script>
<style scoped>
.half {
  display: inline-block;
  width: 50%;
  color: #999999;
}
.right {
  text-align: right;
}
h2 {
  margin-bottom: 10px;
}
</style>

