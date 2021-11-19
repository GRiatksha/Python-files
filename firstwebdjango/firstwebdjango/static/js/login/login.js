$(document).ready(() => {

<!--const signUpButton = document.getElementById('signUp');-->
<!--const signInButton = document.getElementById('signIn');-->
<!--const container = document.getElementById('container');-->

const signUpButton = jQuery('#signUp');
const signInButton = jQuery('#signIn');
const container = $('#container')[0];


signUpButton.click(function() {
	container.classList.add("right-panel-active");
});

signInButton.click(function() {
	container.classList.remove("right-panel-active");
});


<!--signUpButton.addEventListener('click', () => {-->
<!--	container.classList.add("right-panel-active");-->
<!--});-->

<!--signInButton.addEventListener('click', () => {-->
<!--	container.classList.remove("right-panel-active");-->

});