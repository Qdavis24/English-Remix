


let currentPosition = 0;

function slideCards(direction) {
    const carousel = document.getElementById('carousel');
    const cr = document.getElementById('chevron-right');
    const cl = document.getElementById('chevron-left');

    if (direction === 'right' && currentPosition === 0) {
        carousel.style.transform = 'translateX(-100%)';
        currentPosition = -100;
        cr.style.opacity = '0';
        cl.style.opacity = '1';
    } else if (direction === 'left' && currentPosition === -100) {
        carousel.style.transform = 'translateX(0)';
        currentPosition = 0;
        cr.style.opacity = '1';
        cl.style.opacity = '0';
    }
}