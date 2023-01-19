window.onload = (event) => {
    load()
};

function getCookieValue(name) 
{
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) {
        return match[2];
    }
}

function load() {
    const xhttp = new XMLHttpRequest();

    // Define a callback function
    xhttp.onload = function() {
        var response = JSON.parse(xhttp.responseText);
        if(!getCookieValue("id")) {
            var expiryDate = new Date();
            document.cookie = "id=" + response.id + "; expires=" + expiryDate.getMonth() + 1;
        }
        round.innerHTML="Round: " + response.round;
        totalScore.innerHTML="Score: " + response.score;
        prodImg.src=response.img
    }

    // Send a request
    xhttp.open("POST", "processGame");
    xhttp.setRequestHeader("X-CSRFToken", getCookieValue("csrftoken"));
    xhttp.send(JSON.stringify({
        id: getCookieValue("id"), 
    }));

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
        prodImg.src=response.img
        if(response.finished) {
            totalScore.innerHTML="Score: 0";
            finalScore.innerHTML="Your final score was " + response.score
            finalSummary.classList.add('show')
        } else {
            totalScore.innerHTML="Score: " + response.score;
            roundScore.innerHTML="<strong>You scored " + response.roundScore + " points!</strong><br><br>" + "Actual price: " + response.price + "<br> Your guess: " + guess.value + "<br>Score modifier: " + response.modifier
            scoreSummary.classList.add('show')
        }
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

function closeModals() {
    document.querySelectorAll(".modalContainer").forEach(function(element){
        element.classList.remove("show");  // Add the class that you want to add
    });
}

function revealHint() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        var response = JSON.parse(xhttp.responseText);
        hintNum = response.hintNum

        if (hintNum >= 1) {
            if (hintNum >= 2) {
                if (hintNum == 3) {
                    hint3.innerHTML = "Product Price Range " + response.hint3;
                    hint3.style.display = "block"
                }

                hint2.innerHTML = "Product Name: " + response.hint2;
                hint2.style.display = "block"
            }

            hint1.innerHTML = "Product Ratings: " + response.hint1;
            hint1.style.display = "block"
        }
    }

    // Send a request
    xhttp.open("POST", "getHint");
    xhttp.setRequestHeader("X-CSRFToken", getCookieValue("csrftoken"));
    xhttp.send(JSON.stringify({
        id: getCookieValue("id"), 
    }));
}
