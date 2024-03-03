let button = document.getElementById("CreateTask");
let div = document.getElementById("container");
let TaskLimit = 10;
let id = 0;
let TaskCount = 0;
button.onclick = function(){
	TaskCount++;
	id++;
	if(TaskCount <= TaskLimit){
		div.innerHTML += `<br ><input type='text' placeholder='Enter task'><input type='checkbox'>`;
	}else{
		alert("Can create only 10 tasks.");
	}
}
