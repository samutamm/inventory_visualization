<template>
  <div id="app">
    <ProductSearch msg="Inventory visualization"/>
  </div>
</template>

<script>
import ProductSearch from './components/ProductSearch.vue'

export default {
  name: 'app',
  components: {
    ProductSearch
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
