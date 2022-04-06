// Call ajax page refresh
document.addEventListener("DOMContentLoaded", function(event) {
    const REFRESH = 5000;
    let refreshIntervall = setInterval(refreshAjax, REFRESH);
});

function refreshAjax() {
    let ajax = new XMLHttpRequest();
    ajax.open("GET", "/update", true);

    ajax.onreadystatechange = function() {
        if (ajax.readyState == 4 && ajax.status == 200) {
            document.querySelector("tbody").innerHTML = ajax.responseText;
        }};
    ajax.send();
}

function modifyAjax(item, action) {
    let ajax = new XMLHttpRequest();
    ajax.open("GET", "/remove?item=" + item , true);

    ajax.onreadystatechange = function() {
        if (ajax.readyState == 4 && ajax.status == 200) {
            document.querySelector("tbody").innerHTML = ajax.responseText;
        }};
    ajax.send();
}

function addAjax(item) {
    let ajax = new XMLHttpRequest();
    ajax.open("GET", "/add?item=" + item , true);

    ajax.onreadystatechange = function() {
        if (ajax.readyState == 4 && ajax.status == 200) {
            document.querySelector("tbody").innerHTML = ajax.responseText;
        }};
    ajax.send();
}