console.log('Tried getLocation')
var x = document.getElementById("demo");
var widget = document.getElementById("div_id_sample_location").getElementsByClassName("geoposition-widget")[0]

var data_map_options = widget.getAttribute("data-map-option");
var data_marker_options = widget.getAttribute("data-marker-option");
var latInput = document.getElementById("id_sample_location_0");
var lngInput = document.getElementById("id_sample_location_1");

getLocation();
function getLocation() {
    console.log('Tried getLocation function')
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    console.log('Tried getPosition function')
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
        x.innerHTML = "Latitude: " + position.coords.latitude +
        "<br>Longitude: " + position.coords.longitude;
    // latInput.value = lat;
    // lngInput.value = lng;
    data_map_options = { "zooom": 5, "center": { "lat": lat, "lng": lng }, 'mapTypeId': 'satellite'};
    data_marker_options = {
        'position': { 'lat': lat, 'lng': lng},
    };
}

