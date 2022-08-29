var modifier = 1;
document.getElementById("hint").addEventListener("click", revealHint);

var totalScore = document.getElementById('totalScore').value;
var productScore = document.getElementById('totalScore').value;

function getCookieValue(name) 
{
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) {
        return match[2];
    }
    else {
        console.log('--something went wrong---');
    }
}

function calculateScore() {
    var score = 0;
    score = Math.abs(price - document.getElementById('guess').value) * modifier * 500;
    totalScore.innerHTML = totalScore + score;
    return score;
}

function productEstimate(price) {
    return "$" + (Math.random() * price).toFixed(2) + " to $" + ((Math.random() + 1) * price).toFixed(2);
}

var revealHint = (function(prodId) {
    var hints = 0;
    return function(prodId) {
        // Create an XMLHttpRequest object
        const xhttp = new XMLHttpRequest();

        // Define a callback function
        xhttp.onload = function() {
            var response = JSON.parse(xhttp.responseText);
            var name = response.name;
            var ratings = response.ratings;
            var category = response.category;
            var price = response.price.slice(1,-1);
            var url = response.url;

            if (hints == 0) {
                hint1.innerHTML = "Product Ratings: " + ratings;
                hint1.style.display = "block"
                modifier = 0.95;
            } else if (hints == 1) {
                hint2.innerHTML = "Product Name: " + name;
                hint2.style.display = "block"
                modifier = 0.85;
            } else if (hints == 2) {
                hint3.innerHTML = "Product Price Range " + productEstimate(parseFloat(price));
                hint3.style.display = "block"
                modifer = 0.65;
            }
            if(hints < 3) {
                hints++;
            }
        }

        // Send a request
        xhttp.open("POST", "getDBData");
        xhttp.setRequestHeader("X-CSRFToken", getCookieValue("csrftoken"));
        xhttp.send(JSON.stringify({id: prodId}));
    };
})();
