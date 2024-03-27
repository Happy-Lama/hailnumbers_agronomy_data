// Utilities
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useAppStore = defineStore('app', () => {
  const stored_values = ref(null)

  return stored_values;
})

export { useAppStore };
