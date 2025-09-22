const carousel = document.getElementById('phoneCarousel');
const cardsVisible = 5;
let index = 0;

function getCardWidth() {
    const card = carousel.querySelector('.phone-card');
    return card ? card.offsetWidth + 16 : 0; // width + gap
}

function autoSlideHighlight() {
    const cards = carousel.getElementsByClassName('phone-card');

    for (let card of cards) card.classList.remove('active');

    let centerIndex = index + Math.floor(cardsVisible / 2);
    if (centerIndex >= cards.length) centerIndex = centerIndex % cards.length;

    cards[centerIndex].classList.add('active');

    const cardWidth = getCardWidth();
    carousel.style.transform = `translateX(-${index * cardWidth}px)`;

    index++;
    if (index > cards.length - cardsVisible) index = 0;

    setTimeout(autoSlideHighlight, 3000);
}

window.onload = autoSlideHighlight;

function scrollGallery(direction) {
    const cardWidth = getCardWidth();
    index += direction;
    if (index < 0) index = 0;
    if (index > carousel.children.length - cardsVisible) {
        index = carousel.children.length - cardsVisible;
    }
    carousel.style.transform = `translateX(-${index * cardWidth}px)`;
}
