document.getElementById("sendButton").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// Add event listeners for suggestion buttons
document.addEventListener("DOMContentLoaded", function () {
  const suggestionButtons = document.querySelectorAll(".suggestion-btn");
  suggestionButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const userInput = document.getElementById("userInput");
      userInput.value = this.textContent.trim();
      userInput.focus();
    });
  });
});

function sendMessage() {
  console.log("Send button clicked");

  const inputBox = document.getElementById("userInput");
  const message = inputBox.value.trim();

  if (message === "") return;

  const chatHistory = document.getElementById("chatHistory");
  const userMessage = document.createElement("div");
  userMessage.className = "message user-message";
  userMessage.innerHTML = `<div class="message-content"><p>${message}</p></div>`;
  chatHistory.appendChild(userMessage);
  inputBox.value = "";
  chatHistory.scrollTop = chatHistory.scrollHeight;

  document.getElementById("typingIndicator").style.display = "block";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message }),
  })
    .then((response) => response.json())
    .then((data) => {
      setTimeout(() => {
        document.getElementById("typingIndicator").style.display = "none";

        const botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        botMessage.innerHTML = `<div class="message-content"><p>${data.response}</p></div>`;
        chatHistory.appendChild(botMessage);
        chatHistory.scrollTop = chatHistory.scrollHeight;
      }, 2000); // 2-second delay for typing effect
    })
    .catch((err) => {
      document.getElementById("typingIndicator").style.display = "none";
      console.error("Error:", err);
    });
}
