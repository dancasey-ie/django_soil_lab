// Uses HTML5 geolocation feature to set the default geoposition field to the current device location

var default_promt = document.getElementById("default_info");
//var widget = document.getElementById("div_id_sample_location").getElementsByClassName("geoposition-widget")[0]
//var data_map_options = widget.getAttribute("data-map-options")
//var data_marker_options = widget.getAttribute("data-marker-options")

// A bit hacky: checks if the marker has already been set so that the user isnt asked for location access a second time
function checkLocation() {
    if (document.getElementById("id_sample_location_0").value == "") { getLocation() };
}
// Check if geolocation is available
function getLocation() {

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        default_info.innerHTML = "Geolocation is not supported by this browser.";
    }
}

// If geolocation is availabel set the django-geoposition latitude and longidude to the geolocation values
function showPosition(position) {

    var lat = position.coords.latitude;
    var lng = position.coords.longitude;

    var latInput = document.getElementById("id_sample_location_0");
    var lngInput = document.getElementById("id_sample_location_1");

    default_info.innerHTML = "Default location set to your current position";
    latInput.value = lat;
    lngInput.value = lng;
    data_map_options = '{ "zoom": 15, "center": { "lat": ' + lat + ', "lng": ' + lng + ' }, "mapTypeId": "satellite"}';
    data_marker_options = '{ "position": { "lat": ' + lat + ', "lng": ' + lng + ' } }';
   // window.location.reload(false);

}

function useCurrentPos() {


    data_map_options = '{ "zoom": 15, "center": { "lat": ' + 52.1 + ', "lng": ' + (-9.5) + ' }, "mapTypeId": "satellite"}';
    data_marker_options = '{ "position": { "lat": ' + 52.1 + ', "lng": ' + (-9.5) + ' } }';
    console.log(data_marker_options)
   // widget = document.getElementById("div_id_sample_location").getElementsByClassName("geoposition-widget")[0];
   // widget.setAttribute("data-map-options", data_map_options);
   // widget.setAttribute("data-marker-options", data_marker_options);
    $('#div_id_sample_location').$('.geoposition-widget')[0].attr('data-map-options', data_map_options);
    $('#div_id_sample_location').$('.geoposition-widget')[0].attr('data-marker-options', data_marker_options);
    console.log(data_marker_options)

    var marker = new google.maps.Marker(data_marker_options);
}

checkLocation();