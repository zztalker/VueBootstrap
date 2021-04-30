<template>
  <div id="app">b
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
  <b-tabs pills card horisontal>
    <b-tab title="first" active>
     <br>I'm the first fading tab
    </b-tab>
    <b-tab title="second" >
      <b-table id="mtab" :busy.sync="isBusy" striped hover :items="getDataFromFlask" :fields="fields"></b-table>
    </b-tab>
    <b-tab title="disabled" disabled>
      <br>Disabled tab!
    </b-tab>
  </b-tabs>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'app',
  data: {

    msg: 'Добро пожаловать в пример приложения',
    isBusy: false,
    fields: ["col1"]

  },
  methods: {
    getDataFromFlask (ctx) {
        // Here we don't set isBusy prop, so busy state will be handled by table itself
    this.isBusy = true
    let promise = axios.get('/json')
    return promise.then((data) => {
      const items = data.data
      // Here we could override the busy state, setting isBusy to false
      this.isBusy = false
      return(items)
    }).catch(error => {
      // Here we could override the busy state, setting isBusy to false
      // this.isBusy = false
      // Returning an empty array, allows table to correctly handle busy state in case of error
      return []
    })
    }
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

h1, h2 {
  font-weight: normal;
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
