<template>
    <div id="map" style="height: 50vh; ">
    </div>

</template>

<script setup>

import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { watch, ref, onMounted } from 'vue';
import { useAppStore } from '@/store/app';
import axios from 'axios';

//data
const deployed_modules = ref([]);
const map = ref(null)
const mapmarkers = ref([]);
const appStore = useAppStore();


function updateMarkers(){
    // function to place new markers on the map

    console.log('Updating map markers')

    //create marker for each module received
    let locations = []
    
    deployed_modules.value.forEach((module) => {
        
        let mapmarker = L.marker([module.latitude, module.longitude], {
            title: module.module_id
        });
        
        locations.push([module.latitude, module.longitude])

        mapmarker.on('click', () => {
            console.log(mapmarker.options.title)
            appStore.selected_module = mapmarker.options.title
            axios.get(`https://hailnumbers.pythonanywhere.com/api/soilParameters/${mapmarker.options.title}`)
            .then((response) => {
                console.log(response.data);
                appStore.stored_values = response.data;
            })
        })
        mapmarkers.value.push(mapmarker)
    });

    if(locations){
        // reposition map to show all the markers
        console.log(locations)
        let bounds = L.latLngBounds(locations)
        if(map.value){
            map.value.fitBounds(bounds)
        }
    }
}

watch(() => appStore.modules, (newVal, oldVal) => {
    // update the markers on the map
    console.log('Transformers have changed')
    deployed_modules.value = newVal
    updateMarkers();
    mapmarkers.value.forEach((mapmarker)=>{
        mapmarker.addTo(map.value);
        console.log('Added to map')
    });
}) 

onMounted(() => {
    // initialize map
    map.value = L.map('map').setView([0.34759640, 32.58251970], 12);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map.value);
    mapmarkers.value.forEach((mapmarker)=>{
        mapmarker.addTo(map.value);
        console.log('Added to map')
    });

    if(appStore.modules == null){
        // fetch module information from the backend
        axios.get("https://hailnumbers.pythonanywhere.com/api/soilParameters/modules/all/")
        .then((response) => {
        console.log(response.data)
        appStore.modules = response.data
        })
    } else {
        updateMarkers();
    }
});

</script>