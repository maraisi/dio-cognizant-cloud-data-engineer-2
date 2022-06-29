const BASE_URL = "https://thatcopy.pw/catapi/rest/";
const catBtn = document.getElementById('change-cat')


// getCats vai ser uma função assincrona
const getCats = async () => {

    try{      
        const data = await fetch(BASE_URL);
        // a BASE_URL retona outra promise em string que devera ser convertida para json
        const json = await data.json();
        return json.webpurl;

    } catch (e) {
        console.log(e.message);
    }
};


const loadImg = async () => {
    const catImg = document.getElementById('cat');
    catImg.src = await getCats();
}

catBtn.addEventListener('click',loadImg);

loadImg();