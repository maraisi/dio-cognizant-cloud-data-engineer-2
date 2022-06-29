
const botao = document.getElementById('mode-selector');
const h1 = document.getElementById('page-title');

// o getElementsByTagName retorna um array. É necessário especificar o index do elemento
const corpo = document.getElementsByTagName('body')[0];
const rodape = document.getElementsByTagName('footer')[0];

const darkModeClass = 'dark-mode';

//não colocar os () na função, se não executa
botao.addEventListener("click", changeMode);



function changeMode() {
    changeClasses();
    changeText();   
}

function changeClasses(){
    botao.classList.toggle(darkModeClass);
    h1.classList.toggle(darkModeClass);
    rodape.classList.toggle(darkModeClass);
    corpo.classList.toggle(darkModeClass);
}


function changeText(){
    const lightMode = 'Light Mode';
    const darkMode = 'Dark Mode'


    if(h1.classList.contains(darkModeClass)){
        botao.innerText = lightMode;
        h1.innerText = darkMode + ' ON';
        return;
    }

    botao.innerText = darkMode;
    h1.innerText = lightMode + ' ON';
}

