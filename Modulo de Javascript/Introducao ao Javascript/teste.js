// Comentário de uma linha em Javascript

/* Comentátario de
........várias linhas
..............em Javascript */


//|============ VARIÁVEIS =============|

// var preco = 2;
const PRECO = 2;

var desconto = 0.2;

// preco = preço*desconto;

var total = PRECO - desconto;



//|============= FUNÇÕES ================|

function soma(a, b){
    //console.log(a+b);
    return a + b;
}

// para executar a função é necessário chama-la
soma(1, 3);

console.log(soma(2, 5));
//console.log('\n');
console.log('Hello World!');

function returnEvenValues(array){
    let evenNums = [];
    let oddNums = [];
    for(let i = 0; i < array.length; i++){
        if(array[i]%2 == 0){
            evenNums.push(array[i]);
        } else{
            oddNums.push(array[i]);
        }
    }
    console.log('Os números pares são: ',  evenNums);
    console.log('Os números ímpares são: ',  oddNums);
}

let array = [1,2,3,4,5,6,7,9];
returnEvenValues(array);