<template>
    <v-card variant="flat">
        <v-card-title>
            {{ chartTitle }}
        </v-card-title>
        <Line :data="chartData" :options="chartOptions"></Line>   
    </v-card>
</template>

<script setup>
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import { Line } from 'vue-chartjs'
import { ref, watch, onMounted } from 'vue'

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const props = defineProps(['chartData', 'dataType', 'chartTitle'])
const emit = defineEmits(['loaded'])

const chartData = ref({
    labels: [], 
    datasets: []
})


watch(() => props.chartData, (newVal) => {
    // console.log('Old Value', chartData.value)
    chartData.value = {
        labels: newVal.timestamps, 
        datasets: newVal.datasets
    }
})

const chartOptions = ref({
    responsive: true,
    maintainAspectRation: false,
    scales: {
        x: {
            title : {
                display: true,
                text: "Time"
            }, 
            ticks : {
                display: false,
            }
        },
        y: {
            title : {
                display: true,
            },
            ticks : {
                callback: function(value, index, ticks) {
                        if ("npk".includes(props.dataType)){
                            return value.toFixed(2) + " mg/kg";
                        }
                        if(props.dataType === "ec"){
                            return value + " us/cm";
                        }
                        if(props.dataType === "ph"){
                            return value.toFixed(2) + "PH";
                        }
                        if(props.dataType === "temp"){
                            return value.toFixed(2) + " C";
                        }
                        if(props.dataType === "moisture"){
                            return value + "%";
                        }
                        return value;
                    } 
            }
        }
    }
})

</script>
  