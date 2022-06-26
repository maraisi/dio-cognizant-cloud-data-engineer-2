//Tipos Primitivos

//boolean
var vOUF = false;
console.log("console.log(vOUF):", vOUF);
console.log("console.log(typeof(vOUF)): ",typeof(vOUF));

//number
var numberoQualquer = 1;
console.log(numberoQualquer);
console.log(typeof(numberoQualquer));

//string
var nome = "Mara";
console.log(nome);
console.log(typeof(nome));




//Arrays "[]"
let array = ["string", 1, true, ["array1"], ["array2"]];
console.log(array);
console.log(array[0]);
console.log(array[1]);
console.log(array[2]);
console.log(array[4]);


/*

|============== Manipulação de Arrays ================|

forEach() - itera um array
push() - adiciona um item no final do array
pop() - remove um item no final de um array
unshift() - adiciona um item no começo do array
shift() - remove um item no começo do array
indexOf() - retorna o índice de um valor
splice() - remove ou substitui um item pelo índice
slice() - retorna uma parte de um array existente

*/

array.forEach(function(item, index){console.log(item, index)});

array.push('item adicionado com push()');
console.log(array);

array.pop();
console.log(array);

array.unshift('item adicionado com unshift()');
console.log(array);

array.shift();
console.log(array);

console.log("Qual o índice do item 'true' (console.log(array.indexOf(true)): ", array.indexOf(true));

array.splice(0, 2);
console.log("Usando o array.splice(0, 2) sobrou os itens: ", array);

array.unshift("string", 1);

let novoArray = array.slice(0, 3);
console.log(array);
console.log("Usando o array.slice(0, 3) o novo array tem os itens: ", novoArray);


/* 

Objetos "{}"  possuem propriedades e valores que definem suas características. 

Exemplo:
            var xicara = {
                cor:"azul",
                tamanho: "p",
                funcao: tomarCafe()
            }

Para manipular um objeto:

var cor = xicara.cor;
var tamanho = xicara.tamanho

*/


let objeto = {boleano: true, string: "português", numero: 4, array: [1, 2, [4, 5, 6]], objetoInterno: {propiedade: "valor"}}

console.log(objeto.objetoInterno)
console.log(objeto.boleano)

//Desestruturando o objeto

var texto = objeto.string
console.log(texto)

var {string, boleano, numero} = objeto
console.log({string, boleano, numero})



/*
|========= Condicional =========|

        if
        else if
        else




|======= if ternário: condicional de uma linha =======|

        [CONDIÇÃO]?[INSTRUÇÃO-TRUE]:[INSTRUÇÃO-FALSE];

Exemplo:
*/
var jogador1 = 1
jogador1 > 0 ? console.log("marcou ponto"): console.log("não marcou ponto");

var jogador1 = 0
jogador1 > 0 ? console.log("marcou ponto"): console.log("não marcou ponto");



/*========= Condicional usando switch/case =========|

Exemplo:

        switch(${expressao}){
            case 1:
                ${instrução};
                break
            case 2:
                ${instrução};
                break
            default:
                ${instrução};
        }
*/
var jogador2 = 2

var placar;

// if(jogador1 > jogador2){
//     placar = jogador1 > jogador2
// } else if(jogador2>jogador1){
//     placar = jogador2 > jogador1
// }


switch(placar){
    case placar = jogador1 > jogador2:
        console.log("jogador 1 ganhou");
        break
    case placar = jogador1 < jogador2:
        console.log("jogador 2 ganhou");
        break
    default:
        console.log("Empatou");
};


/* Laçoes de repetição

        FOR
        for(variável, condição, incremento){
            declaração
        }

*/

let arrayFor = ['valor1', 'valor2', 'valor3', 'valor4', 'valor5'];

let objetoFor = {propriedade1: 'valor1', propriedade2: 'valor2', propriedade3: 
'valor3', propriedade4:'valor4', propriedade5:'valor5'};

//aqui vai ser imprimido no console variaveis do tipo numero
for(let indice = 0; indice < arrayFor.length; indice++){
    console.log(indice, typeof(indice));
}


/*

FOR IN
        for(variável_de_estado in array/lista){
            declaração
        }

*/

//aqui vai ser imprimido no console variaveis do tipo string
for(i in arrayFor){
    console.log(i, typeof(i));
}


for(i in objetoFor){
    console.log(i, typeof(i));
}

/*

FOR OF
        for(variável_de_estado of array/lista){
            declaração
        }

*/

for(i in objetoFor){
    console.log(i, typeof(i));
}


// FUNÇÃO DECLARATIVA

function funcaoDeclarativa(msg){
    console.log(msg);
};

funcaoDeclarativa('função declarativa');



// EXPRESSÕES DE FUNÇÕES (a nomeação é opcional)

var funcao1 = function funcao1(){
    console.log('função1');
}
funcao1();


var funcao2 = function(){
    console.log('função2');
}
funcao2();


// ARROW FUNCTION são anônimas e não podem ser nomeadas

var funcaoArrow = () => {
    console.log('Arrow funtion');
}

funcaoArrow();

