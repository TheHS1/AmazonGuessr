var modifier = 1;
document.getElementById("hint").addEventListener("click", revealHint);

var totalScore = document.getElementById('totalScore').value;
var productScore = document.getElementById('totalScore').value;


function calculateScore() {
    var score = 0;
    score = Math.abs(price - document.getElementById('guess').value) * modifier * 500;
    totalScore.innerHTML = totalScore + score;
    return score;
}

function productEstimate() {
    return (Math.random() * price).toFixed(2) + " to " + ((Math.random() + 1) * price).toFixed(2);
}

var revealHint = (function() {
    var hints = 0;
    // var title = JSON.parse("{{name|escapejs}}");
    // var price = JSON.parse("{{price|escapejs}}");
    // var ratings = JSON.parse("{{ratings|escapejs}}");
    // var category = JSON.parse("{{category|escapejs}}");
    // var url = JSON.parse("{{url|escapejs}}");
    return function() {
        if (hints == 0) {
            // hint1.innerHTML = "Product Ratings " + ratings;
            hint1.style.display = "block"
            modifier = 0.95;
        } else if (hints == 1) {
            // hint2.innerHTML = "Product Name: " + title;
            hint2.style.display = "block"
            modifier = 0.85;
        } else if (hints == 2) {
            // hint3.innerHTML = "Product Price Range " + productEstimate();
            hint3.style.display = "block"
            modifer = 0.65;
        }
        if(hints < 3) {
            hints++;
        }
    };
})();

function revealHint() {
}
