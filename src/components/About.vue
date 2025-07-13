<template>
  <section>
    <h1>About</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">
      Error: {{ error }}
    </div>
    <div v-else>
      <p>Name: {{ aboutData.name }}</p>
      <p>Email: {{ aboutData.email }}</p>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface AboutData {
  name: string
  email: string
}

const aboutData = ref<AboutData>({ name: '', email: '' })
const loading = ref(true)
const error = ref('')

const fetchAboutData = async () => {
  try {
    loading.value = true
    error.value = ''
    
    // In production, this would be your deployed API endpoint
    // For now, we'll use a placeholder that you can update after deployment
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'
    const response = await fetch(`${apiUrl}/api/about`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    aboutData.value = data
  } catch (err) {
    error.value = err instanceof Error ? err.message : 'Failed to fetch about data'
    console.error('Error fetching about data:', err)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchAboutData()
})
</script>

<style scoped>
.error {
  color: red;
  font-weight: bold;
}
</style>