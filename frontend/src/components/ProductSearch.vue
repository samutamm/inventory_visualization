<template>
  <div>
    <h1>{{ msg }}</h1>
    <h3>Choose product</h3>
    <div>
      <b-form-select v-model="selected" :options="productIdNames" v-on:change="fetchProduct(selected)"></b-form-select>
    </div>
    <div class="small" v-if="showInvetory">
      <line-chart :chart-data="productInventory" ></line-chart>
      <b-table id="inner" striped bordered hover :items="rows"></b-table>
    </div>
  </div>
</template>

<script>
/* eslint-disable */ 
import LineChart from './LineChart.js'
import { BFormSelect, BTable } from 'bootstrap-vue'
import axios from 'axios'

export default {
  name: 'ProductSearch',
  props: {
    msg: String
  },
  components: {
    LineChart, 
    'b-form-select': BFormSelect,
    'b-table': BTable
  },
  data () {
    return {
      selected: null,
      productIdNames:[],
      showInvetory: false,
      productInventory: {
        labels: [],
        datasets: [
          {
            label: '',
            backgroundColor: '#f87979',
            data: []
          }
        ]
      },
      rows:[]
    }
  },
  mounted () {
    this.fetchProductNames()
  },
  methods: {
    fetchProductNames() {
      axios
      .get('http://localhost:5000/api/products')
      .then(response => {
        const idnames = []
        for (var i = 0; i < response.data.ids.length; i++) {
          idnames.push({
            text: "ID : " + response.data.ids[i] + ", NAME :" + response.data.names[i],
            value: response.data.ids[i],
            disabled: false
          })
        }
        this.productIdNames = idnames
      })
    },
    fetchProduct (productId) {
      axios
      .get('http://localhost:5000/api/products/' + productId)
      .then((response) => {
        const rows = response.data.rows
        this.showInvetory = true
        this.productInventory = {
          labels: rows.map(ex => ex[2]),
          datasets: [
            {
              label: rows[0][1],
              backgroundColor: '#f87979',
              data: rows.map(ex => ex[3])
            }
          ]
        }
        this.rows = rows.map(ex => {
          return {product_id: ex[0], product_name: ex[1], date: ex[2], inventory_level: ex[3]}
        })
      })
      .catch(error => {
        console.log(error)
      })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

#inner {
  display: table;
  margin: 0 auto;
}
</style>
