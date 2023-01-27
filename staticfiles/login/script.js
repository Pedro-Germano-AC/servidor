const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


var cadastro_form = document.getElementsByTagName('input')
cadastro_form[1].placeholder = 'Usuário';
cadastro_form[2].placeholder = 'Email';
cadastro_form[3].placeholder = 'Senha';
cadastro_form[4].placeholder = 'Digite a senha novamente';

for (var field in cadastro_form) {
  cadastro_form[field].className += ' form-control'
}


