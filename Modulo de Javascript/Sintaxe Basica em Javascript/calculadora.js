function calculadora(){
    const operacao = Number(prompt('Escolha uma operação:\n 1 - Soma [+]\n 2 - Subtração [-]\n 3 - Multiplicação [*]\n 4 - Divisão Real [/]\n 5 - Divisão Inteira [%]\n 6 - Potenciação [**]\n 7 - Não desejo realizar uma operação'));
 

    if(!operacao || operacao>=8){
        alert('Operação Inválida!');
        calculadora();
    } else{
        if(operacao == 7){
            alert('Até mais!'); 
            return
       
        } else{

        
            let n1 = Number(prompt('Insira o primeiro valor'));
            let n2 = Number(prompt('Insira o segundo valor'));
            let resultado;

            

            if (operacao == 1){
                soma();
            } else if(operacao == 2){
                subtracao();
            } else if(operacao == 3){
                multiplicacao();
            } else if(operacao == 4){
                divisaoReal();
            } else if(operacao == 5){
                divisaoInt();
            } else if(operacao == 6){
                potenciacao();
            };


            novaOperacao();

            
            function soma(){
                resultado = n1 + n2;
                //o uso do sifrão só é possivel através do acento grave `
                alert(`${n1} + ${n2} = ${resultado}`);
            }

            function subtracao(){
                resultado = n1 - n2;
                alert(`${n1} - ${n2} = ${resultado}`);
            }

            function multiplicacao(){
                resultado = n1 * n2;
                alert(`${n1} * ${n2} = ${resultado}`);
            }

            function divisaoReal(){
                resultado = n1 / n2;
                alert(`${n1} / ${n2} = ${resultado}`);
            }

            function divisaoInt(){
                resultado = n1 % n2;
                alert(`O resto da divisão entre ${n1} e ${n2} = ${resultado}`);
            }

            function potenciacao(){
                resultado = n1 ** n2;
                alert(`${n1} ^ ${n2} = ${resultado}`);
            }


            function novaOperacao(){
                let opcao = prompt('Deseja fazer outra operação?\n 1 - Sim\n 2 - Não');

                if (opcao == 1){
                    calculadora();
                } else if( opcao ==2){
                    alert('Até mais!');
                } else{
                    alert('Digite uma opção válida!');
                    novaOperacao();
                }
            }

            
        }

    }

            
    
}

calculadora();
