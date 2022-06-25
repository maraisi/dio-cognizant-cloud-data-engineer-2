const CURRENT_NUMBER = document.getElementById('currentNumber');
let count = 0;

function increment() {
    if (count < 10){
        count ++;
    } else{
        count = 10
    }
    //Para mudar o elemento no documento HTML (.innerHTML)
    CURRENT_NUMBER.innerHTML = count;
}

function decrement() {
    if (count > 0){
        count --;
    } else{
        count = 0
    }
    //Para mudar o elemento no documento HTML (.innerHTML)
    CURRENT_NUMBER.innerHTML = count;
}