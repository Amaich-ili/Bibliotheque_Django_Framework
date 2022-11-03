
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
        if(!cardOne) {
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
        if(matched == 8) {
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
    let arr = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8];
    arr.sort(() => Math.random() > 0.5 ? 1 : -1);
    cartes.forEach((card, i) => {
        card.classList.remove("flip");
        let imgTag = card.querySelector(".back-view img");
        let a = `../static/images/${arr[i]}.jpg`
        imgTag.src = `../static/images/${arr[i]}.jpg`;
        card.addEventListener("click", flipCard);
    });
}
shuffleCard();
cartes.forEach(card => {
    card.addEventListener("click", flipCard);
});