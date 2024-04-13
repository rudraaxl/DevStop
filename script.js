document.addEventListener("mousemove", function(e) {
    const mouseX = e.pageX;
    const mouseY = e.pageY;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    const bluePercentage = (mouseX / windowWidth) * 100;

    const gradientColor = `linear-gradient(to right, rgba(0,0,0,0.8) ${80 - bluePercentage}%, rgba(0,0,${bluePercentage},0.8) ${100 - bluePercentage}%)`;

    document.querySelector(".gradient").style.backgroundImage = gradientColor;
});
document.getElementById('submit-btn').addEventListener('click', function() {
    var answer = document.getElementById('answer-input').value;
    console.log('User answer:', answer);
}