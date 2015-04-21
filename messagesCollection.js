var app = app || {};

app.Messages = Backbone.Collection.extend({
  model: app.Message,

  url: 'http://127.0.0.1:8000/messages/',

  parse: function(response) {
    return response.results;
  },

  sync: function(method, model, options) {
    var that = this;
    var params = _.extend({
      type: 'GET',
      dataType: 'json',
      url: that.url,
      processData: false
    }, options);
    return $.ajax(params);
  },

  // localStorage: new Backbone.LocalStorage("Messages"),
});