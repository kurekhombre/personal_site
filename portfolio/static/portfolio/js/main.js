// Reveal
window.addEventListener('scroll', reveal);

function reveal(){
    var reveals = document.querySelectorAll('.reveal');
    for(var i = 0; i < reveals.length; i++){
        var windowHeight = window.innerHeight;
        var revealTop = reveals[i].getBoundingClientRect().top;
        var revealPoint = 150;

        if(revealTop < windowHeight - revealPoint){
            reveals[i].classList.add('active');
        }
        else{
            reveals[i].classList.remove('active');
        }
    }
}



// MIXITUP FILTER
let mixerPortfolio = mixitup('.project__list', {
    selectors: {
        target: '.project'
    },
    animation: {
        duration: 300
    }
});

// Link Active
const linkWork = document.querySelectorAll('.project__item')

function activeWork(){
    linkWork.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
}

linkWork.forEach((l=> l.addEventListener('click', activeWork)))