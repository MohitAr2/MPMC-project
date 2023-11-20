// Function to send user message and get bot response
function sendMessage() {
    // Get user input
    var userInput = document.getElementById("user-input").value;

    // Display user message in chat body
    displayUserMessage(userInput);

    // Send user input to backend for processing
    sendToBackend(userInput);
}
// Function to display user message in chat body
function displayUserMessage(message) {
    var chatBody = document.getElementById("chat-body");

    var userMessageContainer = document.createElement("div");
    userMessageContainer.className = "chat-message user-message";

    var messageBubble = document.createElement("div");
    messageBubble.className = "message-bubble";
    messageBubble.textContent = message;

    userMessageContainer.appendChild(messageBubble);
    chatBody.appendChild(userMessageContainer);

    // Scroll to the bottom of the chat body
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Function to display bot message in chat body
function displayBotMessage(message) {
    var chatBody = document.getElementById("chat-body");

    var botMessageContainer = document.createElement("div");
    botMessageContainer.className = "chat-message";

    var messageBubble = document.createElement("div");
    messageBubble.className = "message-bubble";
    messageBubble.textContent = message;

    botMessageContainer.appendChild(messageBubble);
    chatBody.appendChild(botMessageContainer);

    // Scroll to the bottom of the chat body
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Function to send user input to backend for processing
function sendToBackend(userInput) {
    // Here, you can make an API call to your backend with the user input
    // For now, let's assume the response is received as 'botResponse'

    var botResponse = "This is a sample response from the backend.";

    // Display bot response in chat body
    displayBotMessage(botResponse);
}