<template>
  <div class="cards">
    <div class="card incidents">
      <h1>{{incident.title}}</h1>
      <div class="incident_item" v-for="i in incident.update_set" :key="i.id">
        <p>{{i.description}}</p>
        <div class="half">{{i.date | timeAgo}}</div>
        <div class="half right">Status: {{i.status}}</div>
      </div>
    </div>
    <router-link :to="{ name: 'Home'}">
      <div class="back">&larr; back</div>
    </router-link>
  </div>
</template>
<script>
import { timeFormatter } from "@/mixins/DateTimeFilters";
export default {
  name: "IncidentDetail",
  mixins: [timeFormatter],
  computed: {
    incident: function() {
      return this.$store.state.incidents.find(
        a => a.id === parseInt(this.$route.params.id)
      );
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

