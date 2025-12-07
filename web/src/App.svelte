<script>
    import { Map } from 'mapbox-gl';
    import 'mapbox-gl/dist/mapbox-gl.css';
    import { onMount, onDestroy } from 'svelte';

    let map;
    let mapContainer;
    let lng, lat, zoom;

    lng = -71.224518;
    lat = 42.213995;
    zoom = 9;

    let initialState = { lng, lat, zoom };

    let fixedLocs = [
        {
            name: "School",
            coordinates: {
                longitude:-83.497626,
                latitude:42.46307
            },
            mapbox_props: {
                mapbox_name: "",
                mapbox_id: "",
                feature_type: "poi",
                address: "11 Madison Ave",
                full_address: "11 Madison Ave, New York, New York 10010, United States",
                place_formatted:"New York, New York 10010, United States",
                routable_points: [
                    {
                        name:"default",
                        latitude:42.46306,
                        longitude:-83.498023
                    }
                ]
            }

        }
    ]

    let POIs = ["gym", "grocery_store", "coffee", "library"]

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

    onMount(() => {
        map = new Map({
            container: mapContainer,
            accessToken: "pk.eyJ1IjoiY2FsbGVuZW5naW5lZXJpbmciLCJhIjoiY21pdXZ6cWJrMXZlNTNlcHZjdnI0bXJtOCJ9.zPcNuWLw7NYrQ2AtPk8Q_g",
            center: [initialState.lng, initialState.lat],
            zoom: initialState.zoom
        });

        map.on('move', () => {
            updateData();
        });
    });

    onDestroy(() => {
        map.remove();
    });
</script>

<div class="map" bind:this={mapContainer}></div>
<div class="sidebar">
Longitude: {lng.toFixed(4)} | Latitude: {lat.toFixed(4)} | Zoom:
{zoom.toFixed(2)}
</div>
<button onclick={handleReset} class="reset-button">Reset</button>

<style>
    .map {
        position: absolute;
        width: 100%;
        height: 100%;
    }

    .sidebar {
      background-color: rgb(35 55 75 / 90%);
      color: #fff;
      padding: 6px 12px;
      font-family: monospace;
      z-index: 1;
      position: absolute;
      top: 0;
      left: 0;
      margin: 12px;
      border-radius: 4px;
    }

    .reset-button {
        position: absolute;
        top: 50px;
        z-index: 1;
        left: 12px;
        padding: 4px 10px;
        border-radius: 10px;
        cursor: pointer;
  }
</style>