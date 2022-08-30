var agency = document.getElementById("agency");
var theme = document.getElementById("theme");
var geo = document.getElementById("geo");
var tag = document.getElementById("tag");

function showagency() {
    agency.style["display"] = "inline";
    theme.style["display"] = "none";
    geo.style["display"] = "none";
    tag.style["display"] = "none";
}
function showtheme() {
    agency.style["display"] = "none";
    theme.style["display"] = "inline";
    geo.style["display"] = "none";
    tag.style["display"] = "none";
}
function showgeo() {
    agency.style["display"] = "none";
    theme.style["display"] = "none";
    geo.style["display"] = "inline";
    tag.style["display"] = "none";
}
function showtag() {
    agency.style["display"] = "none";
    theme.style["display"] = "none";
    geo.style["display"] = "none";
    tag.style["display"] = "inline";
}

window.onbeforeunload = showagency()
