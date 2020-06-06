<template>
  <div id="app">
    <Map />
  </div>
</template>

<script>
import Map from "./components/Map";


export default {
  name: "App",
  components: {
    Map,
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /* background-color: black; */
}
</style>
