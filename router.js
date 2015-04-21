var app = app || {};

app.Router = Backbone.Router.extend({

  routes: {
    // "": 'displayChat',
    //
    "posts/:id": 'getPost'
  },

  displayChat: function() {
    $('#chatContainer').prepend(chatView.render().el);
  },


  getPost: function(id) {
    console.log('looking for post with id: ' + id);
  }
});