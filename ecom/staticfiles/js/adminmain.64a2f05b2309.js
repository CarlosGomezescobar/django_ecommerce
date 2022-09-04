//add hovered calls to select list item
let list = document.querySelectorAll(".navigation li");

function activateLink(){
	list.forEach((item) => {
		item.classList.remove("hovered")
	});
	this.classList.add("hovered");
}
list.forEach((item) => item.addEventListener("mouseover", activateLink));

//Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function (){
	navigation.classList.toggle("active");
	main.classList.toggle("active");
};