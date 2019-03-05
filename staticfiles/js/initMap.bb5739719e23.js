
// Initialises the map view for sample report view
// myLatLng is global variable declared in the viewreport.html template
function initMap() {
    var map = new google.maps.Map(document.getElementById('mymap'), {
        zoom: 15,
        center: myLatLng,
        mapTypeId: 'satellite'
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Sample Site'
    });
        }