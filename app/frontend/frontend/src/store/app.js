// Utilities
import { defineStore } from 'pinia'
import { ref } from 'vue'

const useAppStore = defineStore('app', () => {
  const stored_values = ref(null)
  const modules = ref(null)
  const selected_module = ref(null)
  return stored_values, modules, selected_module;
})

export { useAppStore };
