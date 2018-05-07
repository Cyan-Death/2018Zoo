function showModal(clickedon) {

	document.getElementById(clickedon).style.display = "block"
}

function answer(clickedon) {
	var classToggle = document.getElementById(clickedon);
	classToggle.className = classToggle.className.replace(/\bhidden\b/g,"");
}