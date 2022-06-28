
function substituiNumPar(array){
    //let arraySubs = []; 
    if(!array) return -1;
    if(!array.length) return -1;
    
    for(let i in array){
        if(array[i] % 2 !== 0){
            continue;
            //arraySubs.push(array[i]);
        } else{
            array[i] = 0
            //arraySubs.push(0);
        }
    }
    //return arraySubs;
    return array;
}



//console.log(substituiNumPar(array));
console.log(substituiNumPar([1, 3, 4, 6, 80, 33, 23, 90]));
console.log(substituiNumPar([]));


