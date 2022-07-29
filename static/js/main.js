var title = JSON.parse("{{name|escapejs}}");
var price = JSON.parse("{{price|escapejs}}");
var ratings = JSON.parse("{{ratings|escapejs}}");
var category = JSON.parse("{{category|escapejs}}");
var url = JSON.parse("{{url|escapejs}}");

var hints = 0;
var modifier = 1;
document.getElementById("hint").addEventListener("click", revealHint);

var totalScore = document.getElementById('totalScore').value;
var productScore = document.getElementById('totalScore').value;


function calculateScore() {
    var score = 0;
    score = Math.abs(price - document.getElementById('guess').value) * modifier * 500
    totalScore.innerHTML = totalScore + score;
    return score;
}

function productEstimate() {
    return 0.65 * price + " to " + 1.35 * price;
}

function revealHint() {
    if (hints == 0) {
        hint1.innerHTML = "Product Ratings " + ratings;
        hints = 1;
        modifier = 0.95;
    } else if (hints == 1) {
        hint2.innerHTML = "Product Name: " + title;
        hints = 2;
        modifier = 0.85;
    } else if (hint == 2) {
        hint3.innerHTML = "Product Price Range " + productEstimate();
        hints = 3;
        modifer = 0.65;
    }
}
