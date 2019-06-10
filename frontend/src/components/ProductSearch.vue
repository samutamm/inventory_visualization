<template>
  <div>
    <h1>{{ msg }}</h1>
    <h3>Donut chart</h3>
    <div class="small">
      <line-chart :chart-data="datacollection"></line-chart>
    </div>
  </div>
</template>

<script>
/* eslint-disable */ 
import LineChart from './LineChart.js'
import axios from 'axios'


export default {
  name: 'ProductSearch',
  props: {
    msg: String
  },
  components: {
    LineChart
  },
  data () {
    return {
      datacollection: {
          labels: [],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: []
            }
          ]
        }
    }
  },
  mounted () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      axios
      .get('http://localhost:5000/api/products')
      .then((response) => {
        const rows = response.data.rows
        this.datacollection = {
          labels: rows.map(ex => ex[2]),
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: rows.map(ex => ex[3])
            }
          ]
        }
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
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
</style>
