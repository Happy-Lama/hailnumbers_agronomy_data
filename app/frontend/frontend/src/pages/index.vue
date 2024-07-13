<template>
  <!-- <v-card title="Historical Data Trends and Graphs"> -->
    <MapComponent />
    
    <v-container fluid class="rounded-t-xl position-relative py-5" style="top: -3rem; z-index: 99999; height: 85%;">
      <v-row class="my-2" justify="center">
        <v-col>
          <TimeRangeFilterComponent />
        </v-col>
        <v-col>
          <v-row class="my-2" justify="center">
            <v-col></v-col>
            <v-col>
              <v-btn rounded="lg" size="x-large" block variant="outlined" @click="fetch_pred" class="bg-info">
                Crop Suitability Prediction
              </v-btn>
            </v-col>
            <v-col></v-col>
          </v-row>
          <v-row class="my-2" justify="center">
            <a href="https://hailnumbers.pythonanywhere.com/api/soilParameters/download/" style="text-decoration: none; color: black;">
          <!-- <a href="http://127.0.0.1:8000/api/soilParameters/download/{{appStore.selected_module}}/" style="text-decoration: none;"> -->
              <v-btn rounded="lg" size="x-large" block variant="outlined"  class="bg-info">
                Download Data As CSV
              </v-btn>
            </a>
          </v-row>
        </v-col>
      </v-row>
      <v-row class="my-2" justify="center">
        <v-container fluid v-if="predictions">
          <h1>Crop Suitability Prediction Results</h1>
          <v-container v-for="crop in predictions">
            <v-card class="pa-5 text-h5" variant="outlined">
              <v-row>
                <v-col>
                  {{crop[0]}}
                </v-col>
                <!-- <v-col>
                  <img width="50px" height="50px" alt="crop_image.png" />
                </v-col> -->
              </v-row>
            </v-card>
          </v-container>
          
        </v-container>
      </v-row>
      <v-row justify="center">
        <!-- Two graphs conductivity and ph -->
          <!-- <v-container fluid> -->
          <v-col cols="md-6" class="pa-5">
            <v-container fluid>
              <v-row>
                <!-- conductivity graph -->
                <v-card width="100%" class="mb-2 elevation-1 pr-2">
                  <!-- <v-card-title>Conductivity Graph</v-card-title> -->
                  <ChartComponent :chart-data="conductivity" data-type="ec" chart-title="Conductivity Graph"></ChartComponent>
                </v-card>
              </v-row>
              <!-- <v-spacer vertical></v-spacer> -->
              <v-row>
                <!-- ph graph -->
                <v-card width="100%" class="elevation-1 pr-2">
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
                <v-card width="100%" class="elevation-1 pr-2">
                  <ChartComponent :chart-data="npk" data-type="npk" chart-title="NPK Graph"></ChartComponent>
                </v-card>

              </v-row>

              <v-row class="mt-5 pa-0" align="center" justify="center">
                <v-col cols="md-12" class="pa-1">
                  <!-- temperature -->
                  <v-card class="ma-1 elevation-1 pr-2">
                    <!-- <v-card-title>Temperature Graph</v-card-title> -->
                    <ChartComponent :chart-data="temp" data-type="temp" chart-title="Temperature Graph"></ChartComponent>
                  </v-card>
                </v-col>

                <v-col cols="md-12" class="pa-1">
                  <!-- moisture -->
                  <v-card class="ma-1 elevation-1 pr-2">
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
        
      </v-container>
    </v-container>
  <!-- </v-card> -->
</template>

<script setup>
  
import ChartComponent from '@/components/ChartComponent.vue';
import { onMounted, watch, onBeforeMount } from 'vue';
import { ref } from 'vue';
import { useAppStore } from '@/store/app';
import axios from 'axios';
import MapComponent from '@/components/MapComponent.vue';
import TimeRangeFilterComponent from '@/components/TimeRangeFilterComponent.vue';
// import store from '@/store';

const appStore = useAppStore();

const conductivity = ref({
  timestamps: [],
  datasets: []
})

const predictions = ref(null)

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

const updateValues = (newVal) => {
  // update data with what is received from backend
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
    values.timestamps.push(newVal.timestamp)
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
              data: values.ec,
              tension: 0.6,
              pointRadius: 0
      }]
  }

  temp.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "Temperature", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.temp,
              tension: 0.6,
              pointRadius: 0
      }]
  }

  moisture.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "Moisture", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.moisture,
              tension: 0.6,
              pointRadius: 0
      }]
  }

  ph.value = {
    timestamps: values.timestamps,
    datasets: [
      {
              label: "PH", 
              backgroundColor: "#0000ff",
              borderColor: "#0000ff",
              data: values.ph,
              tension: 0.6,
              pointRadius: 0
      }]
  }

  npk.value = {
    timestamps: values.timestamps,
    datasets: [
      {
        label: "Nitrogen", 
        backgroundColor: "#0000ff",
        borderColor: "#0000ff",
        data: values.npk.n,
        tension: 0.6,
        pointRadius: 0
      },
      {
        label: "Phosphorus", 
        backgroundColor: "#00ff00",
        borderColor: "#00ff00",
        data: values.npk.p,
        tension: 0.6,
        pointRadius: 0
      },
      {
        label: "Potassium", 
        backgroundColor: "#ff0000",
        borderColor: "#ff0000",
        data: values.npk.k,
        tension: 0.6,
        pointRadius: 0
      }
    ]
  }
}

watch(() => appStore.stored_values, (newVal) => {
  updateValues(newVal)      
})


const fetch_pred = () => {
  if(appStore.selected_module){
    // request prediction data from backend
    axios.get(`http://hailnumbers.pythonanywhere.com/api/soilParameters/suitability/${appStore.selected_module}/`). then(
      (response) => {
        console.log(response)
        let recommendations = []
        recommendations.push([response.data.received_data['Most Suitable'][0], "#2eff45"])
        recommendations.push([response.data.received_data['Most Suitable'][1], "#b4da00"])
        recommendations.push([response.data.received_data['Relatively Suitable'][0], "#ebae00"])
        recommendations.push([response.data.received_data['Relatively Suitable'][1], "#ebae00"])
        recommendations.push([response.data.received_data['Least Suitable'][0], "#ff8126"])
        recommendations.push([response.data.received_data['Least Suitable'][1], "#ff5b5b"])

        predictions.value = recommendations
      }
    ).catch(
      (error) => console.log(error)
    )
  } else {
    alert("Select a module first")
  }
}

onMounted(() => {
})


</script>
