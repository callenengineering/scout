<script>
    import Navbar from './components/Navbar.svelte';
    import Map from './components/Map.svelte';

    import data from './data/1007.json'
    import locations from './data/locations.json'
    import preferences from './data/preferences.json'
</script>

<!-- <Navbar /> -->
<Map {data} {locations} {preferences}/>