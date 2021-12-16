var agency = document.getElementById("agency");
var theme = document.getElementById("theme");
var geo = document.getElementById("geo");
var tag = document.getElementById("tag");

function showagency() {
    agency.style["visibility"] = "visible";
    theme.style["visibility"] = "hidden";
    geo.style["visibility"] = "hidden";
    tag.style["visibility"] = "hidden";
}
function showtheme() {
    agency.style["visibility"] = "hidden";
    theme.style["visibility"] = "visible";
    geo.style["visibility"] = "hidden";
    tag.style["visibility"] = "hidden";
}
function showgeo() {
    agency.style["visibility"] = "hidden";
    theme.style["visibility"] = "hidden";
    geo.style["visibility"] = "visible";
    tag.style["visibility"] = "hidden";
}
function showtag() {
    agency.style["visibility"] = "hidden";
    theme.style["visibility"] = "hidden";
    geo.style["visibility"] = "hidden";
    tag.style["visibility"] = "visible";
}

window.onbeforeunload = showagency()
