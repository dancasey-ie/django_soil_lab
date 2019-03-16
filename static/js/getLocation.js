var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};

var geo_error_msg = document.getElementById("geo_error_msg");

function success(pos) {
    var crd = pos.coords;
    var lat = crd.latitude;
    var lng = crd.longitude;

    $("#id_sample_location_0").val(lat).change();
    $("#id_sample_location_1").val(lng).change();
}

function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
    geo_error_msg.innerHTML = "Geolocation is not supported by this browser.";
}

function useCurrentPos() {
    navigator.geolocation.getCurrentPosition(success, error, options);
}


