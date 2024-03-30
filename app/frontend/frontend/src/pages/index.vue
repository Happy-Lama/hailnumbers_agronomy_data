<template>
  <!-- <v-card title="Historical Data Trends and Graphs"> -->
    <v-container fluid>
      
      <v-row justify="center">
        <!-- Two graphs conductivity and ph -->
          <!-- <v-container fluid> -->
          <v-col cols="md-4" class="pa-5">
            <v-container fluid>
              <v-row>
                <!-- conductivity graph -->
                <v-card width="100%" class="mb-2 elevation-7 pr-2">
                  <!-- <v-card-title>Conductivity Graph</v-card-title> -->
                  <ChartComponent :chart-data="conductivity" data-type="ec" chart-title="Conductivity Graph"></ChartComponent>
                </v-card>
              </v-row>
              <!-- <v-spacer vertical></v-spacer> -->
              <v-row>
                <!-- ph graph -->
                <v-card width="100%" class="elevation-7 pr-2">
                  <!-- <v-card-title>PH Graph</v-card-title> -->
                  <ChartComponent :chart-data="ph" data-type="ph" chart-title="PH Graph"></ChartComponent>
                </v-card>
              </v-row>
            </v-container>
          </v-col>
          <!-- <v-spacer></v-spacer> -->
          <!-- Three graphs npk and temperature and moisture -->
          <v-col cols="md-6" class="pa-5">
            <v-container fluid>
              <v-row>

                <!-- npk graph -->
                <v-card width="100%" class="elevation-7 pr-2">
                  <ChartComponent :chart-data="npk" data-type="npk" chart-title="NPK Graph"></ChartComponent>
                </v-card>

              </v-row>

              <v-row class="mt-5 pa-0" align="center" justify="center">
                <v-col cols="md-6" class="pa-1">
                  <!-- temperature -->
                  <v-card class="ma-1 elevation-7 pr-2">
                    <!-- <v-card-title>Temperature Graph</v-card-title> -->
                    <ChartComponent :chart-data="temp" data-type="temp" chart-title="Temperature Graph"></ChartComponent>
                  </v-card>
                </v-col>

                <v-col cols="md-6" class="pa-1">
                  <!-- moisture -->
                  <v-card class="ma-1 elevation-7 pr-2">
                    <!-- <v-card-title>Moisture Content Graph</v-card-title> -->
                    <ChartComponent :chart-data="moisture" data-type="moisture" chart-title="Moisture Content Graph"></ChartComponent>
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-col>
        <!-- </v-container> -->
      </v-row>
      <v-container fluid>
        <v-row class="my-2" justify="space-around">
          <!-- <v-col> -->
          
          <a href="https://hailnumbers-agronomy-data.onrender.com/api/soilParameters/download/" style="text-decoration: none;">
            <v-btn rounded="lg" size="x-large" block variant="outlined">
              Download Data As CSV
            </v-btn>
          </a>
          <!-- </v-container> -->
          <!-- </v-col> -->
        </v-row>
      </v-container>
    </v-container>
  <!-- </v-card> -->
</template>

<script setup>
  
import ChartComponent from '@/components/ChartComponent.vue';
import { onMounted, watch } from 'vue';
import { ref } from 'vue';
import { useAppStore } from '@/store/app';
import axios from 'axios';
// import store from '@/store';

const appStore = useAppStore();

const conductivity = ref({
  timestamps: [],
  datasets: []
})

const npk = ref({
  timestamps: [],
  datasets: []
})

const ph = ref({
  timestamps: [],
  datasets: []
})

const moisture = ref({
  timestamps: [],
  datasets: []
})

const temp = ref({
  timestamps: [],
  datasets: []
})

watch(() => appStore.stored_values, (newVal) => {
  let values = {
    timestamps: [],
    moisture: [],
    ph: [],
    ec: [],
    npk: {
      n: [],
      p: [],
      k: []
    },
    temp: []
  }

  newVal.forEach((newVal) => {
    values.timestamps.push(newVal.id)
    values.moisture.push(newVal.soil_moisture)
    values.temp.push(newVal.soil_temperature)
    values.ec.push(newVal.soil_electrical_conductivity)
    values.ph.push(newVal.soil_ph)
    values.npk.n.push(newVal.soil_nitrogen_content)
    values.npk.p.push(newVal.soil_phosphorus_content)
    values.npk.k.push(newVal.soil_potassium_content)
  })

  conductivity.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "Conductivity", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.ec
      }]
  }

  temp.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "Temperature", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.temp
      }]
  }

  moisture.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "Moisture", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.moisture
      }]
  }

  ph.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "PH", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.ph
      }]
  }

  npk.value = {
    timestamps: values.timestamps,
    datasets: [
      {
        label: "Nitrogen", 
        backgroundColor: "#0000ff",
        borderColor: "#0000ff",
        data: values.npk.n
      },
      {
        label: "Phosphorus", 
        backgroundColor: "#00ff00",
        borderColor: "#00ff00",
        data: values.npk.p
      },
      {
        label: "Potassium", 
        backgroundColor: "#ff0000",
        borderColor: "#ff0000",
        data: values.npk.k
      }
    ]
  }
         
})


// const download_csv = () => {
//   // axios.get('https://hailnumbers-agronomy-data.onrender.com/api/soilParameters/download/')
//   axios.get('http://127.0.0.1:8000//api/soilParameters/download/')
// }

onMounted(() => {
  axios.get("https://hailnumbers-agronomy-data.onrender.com/api/soilParameters/all/")
  // axios.get("http://127.0.0.1:8000/api/soilParameters/all/")
  .then((response) => {
    console.log(response.data)
    appStore.stored_values = response.data
  })
  
})


</script>
