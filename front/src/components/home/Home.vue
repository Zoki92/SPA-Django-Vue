<template>
  <div>
    <div class="cards">
      <div class="card incidents" v-if="openIncidents.length > 0">
        <div class="incident_item" v-for="i in openIncidents" :key="i.id">
          <router-link :to="{ name: 'IncidentDetail', params: { id: i.id }}">
            <IncidentListItem :incident="i"/>
          </router-link>
        </div>
      </div>
      <div class="card status" v-for="i in this.$store.state.sites" :key="i.id">
        <StatusSite :site="i"/>
      </div>
      <div class="calendar">
        <HistoryPart/>
      </div>
    </div>
  </div>
</template>

<script>
import IncidentListItem from "./IncidentListItem.vue";
import StatusSite from "./StatusSite.vue";
import HistoryPart from "./HistoryPart.vue";
export default {
  name: "Home",
  components: { IncidentListItem, StatusSite, HistoryPart },
  computed: {
    openIncidents: function() {
      return this.$store.state.incidents.filter(a => !a.solved);
    }
  }
};
</script>

<style scoped>
.calendar {
  font-family: Montserrat;
  font-weight: 300;
  max-width: 700px;
  margin: 30px auto 0px;
  font-size: 16px;
}
.card.status {
  margin-bottom: 20px;
}
@media only screen and (max-width: 750px) {
  .calendar {
    margin: 10px !important;
  }
}
</style>