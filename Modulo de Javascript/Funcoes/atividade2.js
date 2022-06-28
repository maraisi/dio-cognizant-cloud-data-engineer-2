function calcularIdade(anos){
    return `Daqui a ${anos} anos, ${this.nome} terá ${ this.idade + anos} anos de idade.`;
}

const pessoa1 = {
    nome: 'Ana', 
    idade: 65
}
const pessoa2 = {
    nome: 'João', 
    idade: 26
}
const pessoa3 = {
    nome: 'Clara', 
    idade: 1
}
const pessoa4 = {
    nome: 'Rafa', 
    idade: 36
}
const pessoa5 = {
    nome: 'Afonso', 
    idade: 70
}

//Call: usa a função especificando o objeto e a o parametro da função

console.log(calcularIdade.call(pessoa1, 25));
console.log(calcularIdade.call(pessoa2, 32));
console.log(calcularIdade.call(pessoa3, 18));


//Apply: mesma coisa mas é necessário os colchetes [] para o parametro

console.log(calcularIdade.apply(pessoa4, [40]));
console.log(calcularIdade.apply(pessoa5, [3]));

