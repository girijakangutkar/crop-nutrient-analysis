function initialize() {

    var markers = [];
    var map = new google.maps.Map(document.getElementById('map-canvas'), {
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var defaultBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(-33.8902, 151.1759),
    new google.maps.LatLng(-33.8474, 151.2631));
    map.fitBounds(defaultBounds);

    // Create the search box and link it to the UI element.
    var input = /** @type {HTMLInputElement} */
    (
    document.getElementById('pac-input'));
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var searchBox = new google.maps.places.SearchBox(
    /** @type {HTMLInputElement} */ (input));

    // Listen for the event fired when the user selects an item from the
    // pick list. Retrieve the matching places for that item.
    google.maps.event.addListener(searchBox, 'places_changed', function () {

        var places = searchBox.getPlaces();

        for (var i = 0, marker; marker = markers[i]; i++) {
            marker.setMap(null);
        }

        markers = [];
        var bounds = new google.maps.LatLngBounds();

        for (var i = 0, place; place = places[i]; i++) {

            // Create a marker for each place.
            var marker = new google.maps.Marker({
                map: map,
                draggable:true,
                title: place.name,
                position: place.geometry.location
            });
            
            var latInput = document.getElementsByName('latitude')[0];
            var lngInput = document.getElementsByName('longitude')[0];
            latInput.value = place.geometry.location.lat()
            lngInput.value = place.geometry.location.lng();
            google.maps.event.addListener(marker, 'dragend', function (e) {
                latInput.value = e.latLng.lat();
                lngInput.value = e.latLng.lng();
            });


            markers.push(marker);

            bounds.extend(place.geometry.location);
        }

        map.fitBounds(bounds);
    });
}

initialize();