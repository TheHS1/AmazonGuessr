window.onload = (event) => {
    stepGame()
};

function getCookieValue(name) 
{
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) {
        return match[2];
    }
}

function makeGuess() {
    stepGame()
    scoreSummary.classList.add('show')
}

function stepGame(){
    const xhttp = new XMLHttpRequest();

    // Define a callback function
    xhttp.onload = function() {
        var response = JSON.parse(xhttp.responseText);
        if(!getCookieValue("id")) {
            var expiryDate = new Date();
            document.cookie = "id=" + response.id + "; expires=" + expiryDate.getMonth() + 1;
        }
        hint1.innerHTML = ""
        hint2.innerHTML = ""
        hint3.innerHTML = ""
        round.innerHTML="Round: " + response.round;
        totalScore.innerHTML="Score: " + response.score;
        prodImg.src=response.img
        guess.value=''
    }

    // Send a request
    xhttp.open("POST", "processGame");
    xhttp.setRequestHeader("X-CSRFToken", getCookieValue("csrftoken"));
    xhttp.send(JSON.stringify({
        id: getCookieValue("id"), 
        guess: guess.value,
    }));
}

function closeSummary() {
    scoreSummary.classList.remove('show')
}

function revealHint() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        var response = JSON.parse(xhttp.responseText);
        hintNum = response.hintNum
        hint = response.hint

        if (hintNum == 1) {
            hint1.innerHTML = "Product Ratings: " + hint;
            hint1.style.display = "block"
        } else if (hintNum == 2) {
            hint2.innerHTML = "Product Name: " + hint;
            hint2.style.display = "block"
        } else if (hintNum == 3) {
            hint3.innerHTML = "Product Price Range " + hint;
            hint3.style.display = "block"
        }
    }

    // Send a request
    xhttp.open("POST", "getHint");
    xhttp.setRequestHeader("X-CSRFToken", getCookieValue("csrftoken"));
    xhttp.send(JSON.stringify({
        id: getCookieValue("id"), 
    }));
}
