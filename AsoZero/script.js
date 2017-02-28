var api = 'http://asociacioncero.pythonanywhere.com/api/v1/gato_enfermo/?format_json'
var config = 'http://asociacioncero.pythonanywhere.com/api/v1/configuracion/1/'
var apiTest = 'https://yesno.wtf/'

var results = []

var app = new Vue({
  el: '#app',
  data: {
    results: null,
    configuracion: {}
  },
  methods: {
    sendForm: function () {
      this.$refs.formulario.submit()
    }
  }
})

Vue.http.get(api).then(function(response){
	app.results = response.data['results']
})

Vue.http.get(config).then(function(response){
  app.configuracion = response.data
})