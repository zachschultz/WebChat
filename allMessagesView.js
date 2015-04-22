var app = app || {};

app.allMessagesView = Backbone.View.extend({
  initialize: function(options) {
    _.bindAll(this, 'render');
    this.collection = new app.Messages();
    var theColl = this.collection;
    var that = this;
    var firstMessage = options.firstMessage;
    firstMessage.save();
    this.collection.fetch({
      success: function() {
        that.render();
      }
    });
    this.render();

  },

  template: _.template($('#messagesTemplate').html()),

  render: function() {
    $(this.el).find('#chat').html(this.template({
      messages: this.collection.toJSON()
    }));
    this.$el.show();
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
      this.collection.add(newMsg);
      newMsg.save();
    } else {
      this.collection.remove(newMsg);
      alert("Please enter text!");
    }
    console.log($creator + ": " + $content);
    this.render();
  },

});