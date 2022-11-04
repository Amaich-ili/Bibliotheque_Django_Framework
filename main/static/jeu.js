
/*ce code a été netoyé pour garder ce que j'ai besoin
voici la video ecouté pour faire ce code js: https://www.youtube.com/watch?v=DABkhfsBAWw*/ 
/**/
const cartes = document.querySelectorAll(".card");
let matched = 0;
let carteOne, cardTwo;
let disableDeck = false;
function flipCard({target: clickedCard}) {
    if(cardOne !== clickedCard && !disableDeck) {
        clickedCard.classList.add("flip");
        if(!cardOne){
            return cardOne = clickedCard;
        }
        cardTwo = clickedCard;
        disableDeck = true;
        let cardOneImg = cardOne.querySelector(".back-view img").src,
        cardTwoImg = cardTwo.querySelector(".back-view img").src;
        matchCards(cardOneImg, cardTwoImg);
    }
}
function matchCards(img1, img2) {
    if(img1 === img2) {
        matched++;
        if(matched == 15) {
            document.getElementById("text").innerHTML = "bravo! tu as reussis, appuis sur le boutton pour recommencer."
            document.getElementById("button").style.opacity = 1
        }
        cardOne.removeEventListener("click", flipCard);
        cardTwo.removeEventListener("click", flipCard);
        cardOne = cardTwo = "";
        return disableDeck = false;
    }
    setTimeout(() => {
        cardOne.classList.remove("flip");
        cardTwo.classList.remove("flip");
        cardOne = cardTwo = "";
        disableDeck = false;
    }, 1000);
}
function shuffleCard() {
    document.getElementById("text").innerHTML = ""
    document.getElementById("button").style.opacity = 0
    matched = 0;
    disableDeck = false;
    cardOne = cardTwo = "";
    let arr1 = [1, 2, 3, 4]
    const random = Math.floor(Math.random() * arr1.length);
    var arr = []
    if (random == 1) {
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
    }
    if (random == 2) {
        arr = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
    }
    if (random == 3) {
        arr = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45];
    }
    if (random == 4) {
        arr = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60];
    }
    console.log(arr)

    arr.sort(() => Math.random() > 0.5 ? 1 : -1);
    cartes.forEach((card, i) => {
        card.classList.remove("flip");
        let imgTag = card.querySelector(".back-view img");
        imgTag.src = `../static/images/${arr[i]}.jpg`;
        card.addEventListener("click", flipCard);
    });
}
shuffleCard();
cartes.forEach(card => {
    card.addEventListener("click", flipCard);
});

var data = {"data1":cardOneImg, "data2":cardTwoImg}
// url = "jeu2/"
// console.log(url)
// fetch(url, {
//     method: "POST",
//     headers: {
//     'Accept': 'application/json',
//     'Content-Type': 'application/json' 
// },

// credentials: 'include',

//   //make sure to serialize your JSON body
//   body: JSON.stringify(data)
// })
//   .then((response) => response.json())
//   .then((data) =>   console.log("data1:", data),
//                     console.log("data auteur: ", data.image));