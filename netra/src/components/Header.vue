<template>
  <div class='header-main-div'>
    <img src="../assets/logo.png" alt="logo">
    <ul class='links'>
      <li>
        <a href="#">
          Home
        </a>
      </li>
      <li>
        <a href="#">
          Map
        </a>
      </li>  
      <li>
        <a href="#">
          About
        </a>
      </li>  
    </ul>
  </div>
</template>

<script>

export default {
  name:'Header',

}

</script>

<style scoped>

.header-main-div {
  font-family: monospace;
  background-color: rgb(255, 255, 255);
  color: rgb(109, 109, 109);
  max-height: 100px;
  max-width: 100vw;
}

.header-main-div img {
  margin: 5px 20px 5px 20px;
  width: 50px;
  height: 50px;
  float: left;
}

.links {
  padding: 20px 0 20px 0;
}

.links li {
  display: inline;
  font-size: 20px;
  margin-left: 20px;
  padding: 10px 0 10px 0;
}

.links a {
  color: rgb(56, 56, 56);
  text-decoration: none;
}

.links a:hover {
  color: rgb(119, 119, 119);
}




</style>