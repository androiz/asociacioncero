# Asociacion CERO

This project is a project donated to Asociacion CERO, which help animals in order to be integrated at society, finding a family for them and paying their medical necessities.

## Instalation

First, you need to clone all files from the project with ```git clone url```. Then, you must install the requirements:

```
pip install -r requirements.txt
```

Finally, you have to point the api url to the frontend side. You can configure this from **./AsoZero/script.js** file:

```javascript
var api = '<domain>/api/v1/gato_enfermo/'
var config = '<domain>/api/v1/configuracion/1/'
```

## Official WebSite

You can access to the official web site at [asociacioncero.es](http://asociacioncero.es) so as to help to the organization, not only with donations but also with your support.

### Stuff used to make this:

 * [Vue.js](https://vuejs.org) for integration between the API and the frontend.
 * [Bootstrap](http://getbootstrap.com) for styling the frontend site.
 * [Django](https://www.djangoproject.com) for developing the backend.
 * [django-restframework](http://www.django-rest-framework.org) for developing the API REST.

