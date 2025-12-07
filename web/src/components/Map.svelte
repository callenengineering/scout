<script>
    import { Map, Marker, Popup } from 'mapbox-gl';
    import 'mapbox-gl/dist/mapbox-gl.css';
    import { onMount, onDestroy } from 'svelte';

    let {data , locations, preferences} = $props();

    let map;
    let mapContainer;
    let home_marker;
    let lng = $derived(data.props.coordinates.longitude)
    let lat = $derived(data.props.coordinates.latitude)
    let zoom = $state(9);

    let initialState = {lng, lat, zoom};

    async function fetchData() {
        let res = await fetch('http://localhost:8000/mapping');
        console.log(await res.json())
        console.log(data)
    }

    function updateData() {
        zoom = map.getZoom();
        lng = map.getCenter().lng;
        lat = map.getCenter().lat;
    }

    function handleReset() {
        map.flyTo({
            center: [initialState.lng, initialState.lat],
            zoom: initialState.zoom,
            essential: true
        });

    }

    function calculateDistance(distance) {
        if (preferences.distance === "mi") {
            return Math.round(distance/1609.344).toFixed(1);
        } else if (preferences.distance === "km") {
            return Math.round(distance/1000).toFixed(1);
        } else {
            return distance
        }
    }

    function calculateDuration(duration) {
        return Math.round(duration/60)
    }

    onMount(async () => {
        map = new Map({
            container: mapContainer,
            accessToken: "pk.eyJ1IjoiY2FsbGVuZW5naW5lZXJpbmciLCJhIjoiY21pdXZ6cWJrMXZlNTNlcHZjdnI0bXJtOCJ9.zPcNuWLw7NYrQ2AtPk8Q_g",
            center: [initialState.lng, initialState.lat],
            zoom: initialState.zoom,
        });
        home_marker = new Marker({color: 'red'}).setLngLat([initialState.lng, initialState.lat]).addTo(map);

        locations.fixed.forEach(loc => {
            let marker = new Marker({color: 'green'}).setLngLat([loc.coordinates.longitude, loc.coordinates.latitude]).addTo(map)
            let duration = calculateDuration(data.locations_data[loc.name].duration);
            let distance = calculateDistance(data.locations_data[loc.name].distance);
            const popup = new Popup()
            .setHTML(`<h3>${loc.name}</h3><p>${loc.props.address}</p><p>${duration} min, ${distance} ${preferences.distance}</p>`);

            marker.setPopup(popup);
        })

        map.on('move', () => {
            updateData();
        });

        await fetchData();
    });

    onDestroy(() => {
        map.remove();
    });
</script>

<div class="map" bind:this={mapContainer}></div>
<div class="sidebar">
    Scouting: {data.address}
    <div>
        <input />
        <button>Add</button>
    </div>
    <ul>
        {#each locations.fixed as loc}
            <li>{loc.name} | Distance: {calculateDistance(data.locations_data[loc.name].distance)} {preferences.distance}| Duration: {calculateDuration(data.locations_data[loc.name].duration)} min</li>
        {/each}
    </ul>
    <br />
    <h3>Points of Interest</h3>
    <div>
        <ul>
            {#each locations.pois as poi}
                <li>{poi}</li>
            {/each}
        </ul>
    </div>
</div>
<button onclick={handleReset} class="reset-button">Reset</button>

<style>
    .map {
        position: absolute;
        width: 100%;
        height: 100%;
    }

    .sidebar {
      background-color: rgba(255, 255, 255, 0.9);
      color: black;
      padding: 6px 12px;
      font-family: monospace;
      position: absolute;
      top: 0;
      left: 0;
      margin: 12px;
      border-radius: 4px;
    }

    .sidebar li {
        text-decoration: none;
    }

    .reset-button {
        position: absolute;
        top: 10px;
        z-index: 1;
        right: 12px;
        padding: 4px 10px;
        border-radius: 10px;
        cursor: pointer;
    }
</style>