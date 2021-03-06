$(function() {
  var $chatContainer = $('#chatContainer').hide();
  var $initialDiv = $('div#initialMessage').hide();
  var $initialForm = $initialDiv.find('form#initialForm');

  $initialDiv.fadeIn(2000);

  $initialForm.on('submit', function(e) {
    e.preventDefault();
    $initCreator = $initialDiv.find('input#initialCreator').val();
    $initContent = $initialDiv.find('input#initialContent').val();

    startChat($initCreator, $initContent);
    $(this).hide();

  });

  function startChat(initCreator, initContent) {
    var firstMessage = new app.Message({
      creator: initCreator,
      content: initContent
    });

    var chatView = new app.allMessagesView({
      el: $chatContainer,
      firstMessage: firstMessage
    });

  }



  var router = new app.Router();

  Backbone.history.start();
});