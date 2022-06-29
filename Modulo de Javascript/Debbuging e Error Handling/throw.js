// Funcao original
function verificaPalindromo(string){
    if(!string) return "string inválida";  
    return string.split("").reverse().join("") === string;
}
console.log(verificaPalindromo(''));



// Funcao com throw

function verificaPalindromoThrow(string){
    if(!string) throw "string inválida";  
    return string.split("").reverse().join("") === string;
}
verificaPalindromoThrow('');


// bloco try catch com finally(instrução chamada independente da ocorrência de erro ou não)

function tryCatchExemplo(string){
    try{
        return verificaPalindromoThrow(string)
    } 
    catch(e){
        console.log(e)
        //throw e;
    }
    finally {
        console.log('A string enviada foi: ' + string);
    }
}

tryCatchExemplo('');