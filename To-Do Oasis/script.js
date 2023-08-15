const taskInput = document.getElementById('taskInput');
const pendingList = document.getElementById('pendingList');
const completedList = document.getElementById('completedList');


function addTask() {
    const taskText = taskInput.value.trim();
    if (taskText === '') return;

    const taskItem = document.createElement('li');
    taskItem.innerHTML = `
        <span>${taskText}</span>
        <button onclick="completeTask(this)">Complete</button>
        <button onclick="removeTask(this)">Remove</button>
    `;
    pendingList.appendChild(taskItem);
    taskInput.value = '';
}


function completeTask(button) {
    const taskItem = button.parentElement;
    taskItem.querySelector('button').remove();
    taskItem.querySelector('span').classList.add('completed');
    completedList.appendChild(taskItem);
}


function removeTask(button) {
    const taskItem = button.parentElement;
    taskItem.remove();
}
