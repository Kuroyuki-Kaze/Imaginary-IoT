function sendxhr(status, url) {
    var data = JSON.stringify({
        "action": status
    });

    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", () => {
        if (this.readyState == 4) {
            console.log(this.responseText);
        }
    });

    xhr.open("POST", url);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data)
}

function switch_on() {
    sendxhr("on", "http://localhost:5000/submit");

    history.go(0);
}

function switch_off() {
    sendxhr("off", "http://localhost:5000/submit");

    history.go(0);
}

function grabstats() {
    var xhr = new XMLHttpRequest();
    xhr.addEventListener("readystatechange", () => {
        if (this.readyState == 4) {
            console.log(this.responseText);
            document.getElementById("stats").innerHTML = `Status = ${this.responseText}`
        }
    });

    xhr.open("GET", "http://localhost:5000/home/")
}