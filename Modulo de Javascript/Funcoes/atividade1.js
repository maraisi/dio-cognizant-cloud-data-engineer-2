const arrayAlunos = [
    {
        nome: 'Ana',
        nota: 7
    },
    {
        nome: 'João',
        nota: 3
    },
    {
        nome: 'Lucia',
        nota: 5
    },
    {
        nome: 'Carlos',
        nota: 9
    },
    {
        nome: 'Vitor',
        nota: 7
    },
    {
        nome: 'Silvia',
        nota: 4
    }
]


// function alunosAprovados(arrayAlunos, mediaFinal){
   
//     let arrayAprovados = [];

//     for (let i = 0; i < arrayAluno.length; i++){
//         if(arrayAlunos[i].nota >= mediaFinal){
//             arrayAprovados.push(arrayAlunos[i].nome);
//         }
//     }
//     return alunoAprovados;
//}




function alunosAprovados(array, mediaFinal){
   
    let arrayAprovados = [];

    for (let i = 0; i < array.length; i++){
        // Usando object destructuring (utilizar somente as propriedades que precisamos)
        const {nome, nota} = array[i];
        if(nota >= mediaFinal){
            arrayAprovados.push(nome);
        }
    }
    return arrayAprovados;
}

console.log(alunosAprovados(arrayAlunos, 5));