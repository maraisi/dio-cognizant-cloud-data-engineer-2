function validaArray(array, num) {
   
    try {

        if (!array && !num) throw new ReferenceError("Envie os parâmetros corretos");
        
        if (typeof(array) !== 'object') throw new TypeError("O array precisa ser do tipo object");
        
        if (typeof(num) !== 'number') throw new TypeError("O array precisa ser do tipo number");
        
        if (array.length !== num) throw new RangeError("O tamanho do array é inválido");
        return array;
  
    } catch(e) {
  
        if (e instanceof ReferenceError) {
            console.log("Este erro é do tipo ReferenceError");
            console.log(e.message);
        } 
    
        else if (e instanceof TypeError) {
            console.log("Este erro é do tipo TypeError");
            console.log(e.message);
        } 
    
        else if (e instanceof RangeError) {
            console.log("Este erro é do tipo RangeError");
            console.log(e.message);
        }  
        
        else {
            console.log("Tipo de erro não esperado: " + e);
        }
  
    }
  
  } 
  
  
  console.log(validaArray());