<template>
    <form>
        <v-card>
            <v-container class="datetime_container">
                <v-row>
                    <v-col>
                        <p>
                            <label for="startdatetime">Start Date and Time</label>
                        </p>
                        <input type="datetime-local" id="startdatetime" name="startdatetime" v-model="startDate" class="datetime" defaultValue="">
                    </v-col>
                    <v-col>
                        <p>
                            <label for="enddatetime">End Date and Time</label>
                        </p>
                        <input type="datetime-local" id="enddatetime" name="enddatetime" v-model="endDate" class="datetime">
                    </v-col>
                </v-row>
            </v-container>
            <v-btn rounded="lg" size="x-large" block variant="outlined" class="bg-info" @click="filter()">
                Filter
            </v-btn>
        </v-card>
        
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
        // send request to backend for data in the updated time range
        console.log(startDate.value, endDate.value);
        axios.get(`https://hailnumbers.pythonanywhere.com/api/soilParameters/${appStore.selected_module}/?startDate=${startDate.value}&endDate=${endDate.value}&`)
        .then((response) => {
            console.log(response.data);
            // save the received data
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
    /* box-shadow: 2px 3px 9px -3px black; */
}
form .v-btn{
    margin-top: 1rem;
}

.datetime{
    border: 1px solid black;
    border-radius: 5px;
    padding: 5px
}

</style>