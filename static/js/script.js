document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const chatbox = document.getElementById('chatbox');

    sendButton.addEventListener('click', () => {
        const messageText = userInput.value.trim();
        if (messageText) {
            displayMessage(messageText, 'user');
            userInput.value = '';

            // Send message to backend
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: messageText }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                if (data.reply) {
                    displayMessage(data.reply, 'ai');
                } else {
                    displayMessage('AI: Sorry, I could not understand that.', 'ai');
                }
            })
            .catch(error => {
                console.error('Error sending message:', error);
                displayMessage('Error: Could not connect to the AI. Please try again later.', 'ai');
            });
        }
    });

    function displayMessage(messageText, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.classList.add(sender === 'user' ? 'user-message' : 'ai-message');
        messageElement.textContent = messageText;
        chatbox.appendChild(messageElement);
        chatbox.scrollTop = chatbox.scrollHeight; // Scroll to bottom
    }

    // Optional: Allow sending message by pressing Enter key
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendButton.click(); // Trigger the send button's click event
        }
    });
});
