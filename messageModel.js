var app = app || {};

app.Message = Backbone.Model.extend({

  url: 'http://127.0.0.1:8000/makemessage/',

  initialize: function() {
    console.log(this.get('creator') + " has created a new message: " + this.get('content'));
    this.bind('invalid', function(model, error) {
      console.log(error);
    });
  },
  defaults: {
    'creator': 'NO_CREATOR',
    'content': 'NO_CONTENT',
    'date': (function() {
      var today = new Date();
      var dd = today.getDate();
      var mm = today.getMonth() + 1;
      var yyyy = today.getFullYear();
      if (dd < 10) {
        dd = '0' + dd;
      }
      if (mm < 10) {
        mm = '0' + mm;
      }
      today = mm + '/' + dd + '/' + yyyy;
      return today;
    })()
  },
  validate: function(attrs) {
    if (attrs.message === "")
      return "ERROR: Message needs to have content!";
  },
});