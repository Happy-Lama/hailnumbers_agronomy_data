<template>
    <form>
        <v-card>
            <v-container>
                <v-row>
                    <v-col>
                        <p>
                            <label for="startdatetime">Start Date and Time</label>
                        </p>
                        <input type="datetime-local" id="startdatetime" name="startdatetime" v-model="startDate" class="border border-sm">
                    </v-col>
                    <v-col>
                        <p>
                            <label for="enddatetime">End Date and Time</label>
                        </p>
                        <input type="datetime-local" id="enddatetime" name="enddatetime" v-model="endDate" class="border border-sm">
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
        <v-btn @click="filter()">Filter</v-btn>
    </form>
</template>

<script setup>

import { watch, ref } from 'vue';
import axios from 'axios';
import { useAppStore } from '@/store/app';

const appStore = useAppStore();
const startDate = ref(null);
const endDate = ref(null);

const filter = () => {
    if(startDate.value && endDate.value && appStore.selected_module != null){
        console.log(startDate.value, endDate.value);
        // axios.get(`http://127.0.0.1:8000/api/soilParameters/${appStore.selected_module}/?startDate=${startDate.value}&endDate=${endDate.value}&`)
        // axios.get(`https://hailnumbers-agronomy-data.onrender.com/api/soilParameters/${appStore.selected_module}/?startDate=${startDate.value}&endDate=${endDate.value}&`)
        axios.get(`https://hailnumbers.pythonanywhere.com/api/soilParameters/${appStore.selected_module}/?startDate=${startDate.value}&endDate=${endDate.value}&`)
        .then((response) => {
            console.log(response.data);
            appStore.stored_values = response.data;
        })

    } else{
        alert("Fill in the startDate and endDate or make sure you have selected a module")
    }
}

</script>

<style scoped>
form{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;

}

form > .v-card > input {
    padding: 10px;
}
form .v-card{
    margin: 1rem;
    padding: 0.7rem;
    font-size: 18px;
}
form .v-btn{
    margin-top: 1rem;
}
</style>