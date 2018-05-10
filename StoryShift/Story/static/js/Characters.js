function showModal(clickedon) {

	document.getElementById(clickedon).style.display = "block"
}

function closeModal(clickedon) {

	document.getElementById(clickedon).style.display = "none"
}

function answer(clickedon) {
	var classToggle = document.getElementById(clickedon);
	classToggle.className = classToggle.className.replace(/\bhidden\b/g,"");
}

function dialougueTwo(clickedon) {
	var classToggle = document.getElementById(clickedon);
	classToggle.className = classToggle.className.replace(/\bhidden\b/g,"");
}

function answerTwo(clickedon) {
	var classToggle = document.getElementById(clickedon);
	classToggle.className = classToggle.className.replace(/\bhidden\b/g,"");
}

function dialougueThree(clickedon) {
	var classToggle = document.getElementById(clickedon);
	classToggle.className = classToggle.className.replace(/\bhidden\b/g,"");
}

function answerThree(clickedon) {
	var classToggle = document.getElementById(clickedon);
	classToggle.className = classToggle.className.replace(/\bhidden\b/g,"");
}

