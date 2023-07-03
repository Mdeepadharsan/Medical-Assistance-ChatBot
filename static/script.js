$(document).ready(function() {
    const chatArea = $('#chat-area');
    const chatForm = $('#chat-form');
    const chatInput = $('#chat-input');
  
    chatForm.submit(function(event) {
      event.preventDefault();
      const userMessage = chatInput.val().trim();
      if (userMessage === '') {
        return;
      }
      const userMessageElement = $('<div>').addClass('user-message').text(userMessage);
      chatArea.append(userMessageElement);
      chatInput.val('');
      $.ajax({
        url: '/message',
        type: 'POST',
        dataType: 'json',
        data: { text: userMessage },
        success: function(data) {
          const botMessageElement = $('<div>').addClass('bot-message').text(data.message);
          chatArea.append(botMessageElement);
          chatArea.scrollTop(chatArea[0].scrollHeight);
        },
        error: function(xhr, textStatus, errorThrown) {
          console.error(errorThrown);
        }
      });
    });
  });
  