     // Initialiser la carte et la centrer sur une coordonnée (ex: Paris)
        var map = L.map('map').setView([48.8566, 2.3522], 13);

        // Ajouter les tuiles OpenStreetMap
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Ajouter un marqueur sur la carte
        var marker = L.marker([48.8566, 2.3522]).addTo(map)
            .bindPopup('Paris, France')
            .openPopup();

        // Ajouter un cercle sur la carte
        var circle = L.circle([48.8566, 2.3522], {
            color: 'red',
            fillColor: 'yellow',
            fillOpacity: 0.5,
            radius: 500
        }).addTo(map).bindPopup('Cercle autour de Paris');

        // Ajouter un popup lors d'un clic
        var popup = L.popup();

        function onMapClick(e) {
            popup
                .setLatLng(e.latlng)
                .setContent("Coordonnées cliquées : " + e.latlng.toString())
                .openOn(map);
        }

        map.on('click', onMapClick);