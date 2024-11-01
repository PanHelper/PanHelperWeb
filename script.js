const chatBody = document.querySelector(".chat-body")
const messageInput = document.querySelector(".message-input")
const sendMessageButton = document.querySelector("#send-message")

const userData = {
    message: null
}
const createMessageElement = (content, classes) =>{
    const div = document.createElement("div");
    div.classList.add("message", classes);
    div.innerHTML = content;
    return div;
}
//Outgoing messages
const HandleOutgoingMessage = (e) => {
    e.preventDefault();
    userData.message = messageInput.value.trim();

    //Create and displays user messages
    const messageContent = `<div class="message-text">${userData.message}</div>`;
    const outgoingMessageDiv = createMessageElement(messageContent, "user-message");
    chatBody.appendChild(outgoingMessageDiv);
}

//Allows enter to also be used when sending messages
messageInput.addEventListener("keydown", (e) => {
    const userMessage = e.target.value.trim();
    if (e.key === "Enter" && userMessage) {
        HandleOutgoingMessage(userMessage);
    }
});

sendMessageButton.addEventListener("click", (e) => HandleOutgoingMessage(e));