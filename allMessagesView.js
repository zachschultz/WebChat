var app = app || {};

app.allMessagesView = Backbone.View.extend({
  initialize: function() {
    _.bindAll(this, 'render');
    this.collection = new app.Messages();
    var that = this;
    this.collection.fetch({
      success: function() {
        that.render();
      }
    });
  },

  template: _.template($('#messagesTemplate').html()),

  render: function() {
    console.log(this.collection.toJSON());
    $(this.el).find('#chat').html(this.template({
      messages: this.collection.toJSON()
    }));
  },

  events: {
    'click input#submitMessage': 'addMessage',
    'click #clearChat': 'clearChat',
  },

  clearChat: function() {
    console.log('sup');
  },

  addMessage: function(e) {
    e.preventDefault();

    var $creator = $('input#creator').val();
    var $content = $('input#content').val();
    var newMsg = new app.Message();
    var isValid = newMsg.set({
      'creator': '' + $creator + '',
      'content': $content
    }, {
      validate: true
    });
    if (isValid) {
      newMsg.set({
        'creator': $creator,
        'content': $content
      });
      chatMessages.add(newMsg);
      newMsg.save();
    } else {
      chatMessages.remove(newMsg);
      alert("Please enter text!");
    }
    console.log($creator + ": " + $content);
    this.render();
  },

  // render: function() {

  //   this.$('#chat').html('');
  //   this.$('input#user').val('');
  //   this.$('input#message').val('');
  //   this.collection.each(this.displayMessage, this);
  //   return this;
  // },

  // displayMessage: function(message) {
  //   var messageView = new app.messageView({
  //     model: message
  //   });
  //   this.$('#chat').append(messageView.render().el);
  // }
});