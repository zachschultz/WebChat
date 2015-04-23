var app = app || {};

app.allMessagesView = Backbone.View.extend({

  initialize: function(options) {

    _.bindAll(this, 'render');
    this.collection = new app.Messages();
    theColl = this.collection;
    var that = this;
    var firstMessage = options.firstMessage;
    $('input#creator').val(firstMessage.get('creator'));

    firstMessage.save();

    theColl.on('add', this.render, this);
    theColl.on('reset', this.render, this);
    this.render();

    window.setInterval(function() {
      theColl.fetch({
        // reset: true,
        success: function() {
          that.render();
        }
      });
    }, 3000);


  },

  template: _.template($('#messagesTemplate').html()),

  render: function() {
    console.log(theColl);

    $(this.el).find('#chat').html(this.template({
      messages: theColl.toJSON()
    }));

    var $chat = $(this.el).find('#chat');
    $chat.scrollTop($chat[0].scrollHeight);
    this.$el.show();
  },

  events: {
    'click input#submitMessage': 'addMessage',
    'click #clearChat': 'clearChat',
  },

  clearChat: function() {
    // console.log('sup');
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
      newMsg.save();
      // theColl.add(newMsg);

    } else {
      theColl.remove(newMsg);
      alert("Please enter text!");
    }
    $('input#content').val('');

  },

});