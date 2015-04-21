var app = app || {};

app.messageView = Backbone.View.extend({

  tagName: 'article',
  className: 'messageItem',

  template: _.template($('#messageElement').html()),

  render: function() {
    var messageTemplate = this.template(this.model.toJSON());
    this.$el.html(messageTemplate);
    return this;
  }
});