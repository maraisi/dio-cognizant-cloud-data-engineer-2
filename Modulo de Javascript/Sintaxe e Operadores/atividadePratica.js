
function comparaNums(n1, n2){
    var n1 = Number(prompt('Insira o primeiro número'));
    var n2 = Number(prompt('Insira o segundo número'));


    var igualdade;
    var soma = n1 + n2;
    var somatorio;



    // if (n1 === n2){
    //     igualdade =  `Os números ${n1} e ${n2} são iguais.`
    // } else{
    //     igualdade =  `Os números ${n1} e ${n2} não são iguais.`}


    n1 === n2 ? igualdade =  `Os números ${n1} e ${n2} são iguais.`: igualdade =  `Os números ${n1} e ${n2} não são iguais.`
        
    



    if (soma < 10){
        somatorio = `Sua soma é ${soma}, que é menor que 10 e menor que 20.`

    } else if(soma > 10 && soma < 20) {
        somatorio = `Sua soma é ${soma}, que é maior que 10 e menor que 20.`

    } else if(soma > 10 && soma > 20) {
        somatorio = `Sua soma é ${soma}, que é maior que 10 e maior que 20.`

    } else if(soma === 10) {
        somatorio = `Sua soma é ${soma}, que é igual a 10 e menor que 20.`

    } else if(soma === 20) {
        somatorio = `Sua soma é ${soma}, que é maior que 10 e igual a 20.`
    } else{
        somatorio = `Sua soma é ${soma}, que é maior que 10 e maior que 20.`
    }

    alert(`${igualdade} ${somatorio}`);



}

comparaNums();

