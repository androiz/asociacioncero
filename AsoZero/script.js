var apiSC = 'http://asociacioncero.pythonanywhere.com/api/v1/gato_enfermo/?format_json'
var apiHE = 'http://asociacioncero.pythonanywhere.com/api/v1/gato_final_feliz/?format_json'
var config = 'http://asociacioncero.pythonanywhere.com/api/v1/configuracion/1/'
var apiSCTest = 'http://localhost:8000/api/v1/gato_enfermo/?format_json'
var apiHETest = 'http://localhost:8000/api/v1/gato_final_feliz/?format_json'
var configTest = 'http://localhost:8000/api/v1/configuracion/1/'

var results = []

var app = new Vue({
  el: '#app',
  data: {
    sick_cats: null,
    happy_ending_cats: null,
    configuracion: {}
  },
  methods: {
    sendForm: function () {
      this.$refs.formulario.submit()
    }
  }
})

Vue.http.get(apiSC).then(function(response){
	app.sick_cats = response.data['results']
})

Vue.http.get(apiHE).then(function(response){
	app.happy_ending_cats = response.data['results']
})

Vue.http.get(config).then(function(response){
  app.configuracion = response.data
})
