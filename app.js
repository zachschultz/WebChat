var chatMessages = new app.Messages();
// get existing chats
chatMessages.fetch();



var chatView = new app.allMessagesView({
  // collection: chatMessages
  el: $('#chatContainer')
});


var router = new app.Router();

Backbone.history.start();