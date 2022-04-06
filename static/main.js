function refreshAjax(name) {
    let ajax = new XMLHttpRequest();
    ajax.open("GET", "/update", true);

    ajax.onreadystatechange = function() {
        if (ajax.readyState == 4 && ajax.status == 200) {
            document.querySelector("tbody").innerHTML = ajax.responseText;
        }};
    ajax.send();

    console.log("Update für " + name);
}