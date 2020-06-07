<template>
  <div class='header-main-div'>
    <img src="../assets/logo.png" alt="logo">
    <ul class='links'>
      <li>
        <a href="#" @click = "send_data('navigation')" class = "menu"> 
          Navigation
        </a>
      </li>
      <li>
        <a href="#" @click = "send_data('obstruction')" class = "menu">
          Refresh
        </a>
      </li>  
    </ul>
  </div>
</template>

<script>

export default {
  name:'Header',
  methods: {
    send_data(display_view){
      this.$emit("display_view", display_view)
    }
  }

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



.menu{
  padding: 5px 5px 5px 5px;
  border: black solid 1px;
  border-radius: 5px;
}

.menu:hover{
  color: white;
  background-color: brown;
  font-weight: bolder;
}




</style>