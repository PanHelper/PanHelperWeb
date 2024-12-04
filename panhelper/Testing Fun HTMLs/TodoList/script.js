//Getting all required elements
const inputField = document.querySelector(".input-field textarea"),
ToDoLists = document.querySelector(".ToDoLists"),
pendingNum = document.querySelector(".pending-num"),
clearButton = document.querySelector(".clear-button");

function allTasks() {
    let tasks = documument.querySelector(".pending");
    console.log(tasks); 
}

//adding tasks while we put value in text area and press enter
inputField.addEventListener("keyup", (e) => {
    let inputVal = inputField.value.trim();

    if (e.key === "Enter" && inputVal.length > 0) {
        let liTag = ` <li class="list pending" onclick="handleStatus(this)">
                <input type="checkbox" />
                <span class="task">${inputVal}</span>
                <i class="uil uil-trash"></i>
            </li>`;
    
    ToDoLists.insertAdjacentElement("beforeend", liTag); 
    inputField.value = "";
    allTasks(); 
    }
})

function handleStatus(e) {
    const checkbox = e.querySelector("input");
    checkbox.checked = checkbox.checked ? false : true;
    e.classList.toggle("pending");
}