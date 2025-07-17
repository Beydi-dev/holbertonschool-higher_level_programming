#!/usr/bin/node

// Script that updates the text color of the header element when the user clicks on the tag

document.getElementById('red_header').onclick = function () {
	document.querySelector('div').style.color = '#FF0000';
};
