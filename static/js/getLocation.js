var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};

function success(pos) {
    var crd = pos.coords;
    var lat = crd.latitude;
    var lng = crd.longitude;

    $("#id_sample_location_0").val(lat).change();
    $("#id_sample_location_1").val(lng).change();
    window.location.reload(false);
}

function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
}

function useCurrentPos() {
    navigator.geolocation.getCurrentPosition(success, error, options);

}
