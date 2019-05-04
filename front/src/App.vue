<template>
  <div id="app">
    <NotificationBar/>
    <TheHeader/>
    <router-view/>
    <TheFooter/>
  </div>
</template>

<script>
import NotificationBar from "@/components/general/NotificationBar";
import TheHeader from "@/components/general/TheHeader";
import TheFooter from "@/components/general/TheFooter";
export default {
  name: "App",
  components: {
    NotificationBar,
    TheFooter,
    TheHeader
  }
};
</script>

<style>
body {
  font-family: Montserrat;
}
body,
html {
  margin: 0px;
  padding: 0px;
}
h2,
h3,
h1,
h4 {
  margin-top: 5px;
  margin-bottom: 5px;
}
a,
a:focus,
a:visited,
a:hover {
  color: #000;
  text-decoration: none;
}
.issue,
.yellow {
  background: #f1c21a;
}
.down,
.red {
  background: #cd5c5c;
}
.up,
.green {
  background: #2ee779;
}
.cards {
  margin-top: -30px;
  max-width: 700px;
  margin: -30px auto 20px;
}
.card {
  border-radius: 10px;
  background-color: white;
  padding: 15px 20px;
  box-shadow: 0 0 3px 1px rgba(163, 163, 163, 0.3);
  -webkit-box-shadow: 0 0 3px 1px rgba(163, 163, 163, 0.3);
  font-family: Montserrat;
  font-weight: 300;
}
.incidents > .incident_item {
  margin-bottom: 30px;
  margin-top: 10px;
}
.incidents > .incident_item:last-child {
  margin-bottom: 10px;
}
.incidents {
  margin-bottom: 30px;
}
</style>
