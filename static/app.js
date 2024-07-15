$(document).ready(function() {
    $('#chat-form').submit(function(event) {
        event.preventDefault();
        var userInput = $('#user-input').val();

        $.ajax({
            type: 'POST',
            url: '/chat',
            contentType: 'application/json',
            data: JSON.stringify({ input_text: userInput }),
            success: function(response) {
                var chatBox = $('#chat-box');
                chatBox.append('<p class="user-message">' + userInput + '</p>');
                chatBox.append('<p class="bot-message">' + response.response + '</p>');
                $('#user-input').val('');
                chatBox.scrollTop(chatBox[0].scrollHeight); // Auto-scroll to bottom
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    });
});