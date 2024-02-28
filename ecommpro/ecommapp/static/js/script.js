currentslideid = 0;

const sliderElement = document.getElementById('slider');
const totalSlider = sliderElement.childElementCount

function next() {
    if(currentslideid < totalSlider  ){
    currentslideid++;
    showSlide();
    }
    console.log("clicked");
}

function prev() {
    if(currentslideid  > 1){
        currentslideid--;
        showSlide();
        }
        console.log("clicked");
}

function showSlide() {
    slides =document.getElementById('slider').getElementsByTagName('li');
    for(let index = 0;index < totalSlider;index++){
        const element = slides[index]
        if(currentslideid === index+1){
            element.classList.remove('hidden');
        }else{
            element.classList.add('hidden');
        }
    }
    console.log('show');
    
}
function autoply() {
    next();
    if(currentslideid >= totalSlider  ){
        currentslideid = 1 ;
    }
    setTimeout(()=>{
        autoply(); 
    },1000)
}

setTimeout(()=>{
    autoply(); 
},3000)