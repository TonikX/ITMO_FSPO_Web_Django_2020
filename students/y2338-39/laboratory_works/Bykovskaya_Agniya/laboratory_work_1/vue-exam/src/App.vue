<template>
  <div id="app">
    <router-view/>
  </div>
</template>


<script>
  export default {
    name: 'App'
  }
</script>


<style>
#app {
  font-family: Century Gothic,  sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}

   table{
     margin-top: 40px;
     width: 900px;
     border-collapse: collapse;
     overflow: hidden;
     box-shadow: 0 0 20px rgba(0,0,0,0.1);
     text-align: center;

     border-radius: 10px;
    font-size: 12px;
    font-weight: normal;
    border: #201e7b;
    white-space: nowrap;
    background-color: #a9ceea;
}

td, th {
    text-align: center;
    padding: 8px;
}

td {
    font-size: 13px;
}

thead th {
    color: #ffffff;
    background: #B6CEB7;
}

tr:nth-child(odd) {
    background: #E3DDDD;
}
tr:nth-child(even) {
    background: #EEE9E8;
}
</style>
