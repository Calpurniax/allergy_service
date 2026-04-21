<script setup lang="ts">

defineProps<{
  modelValue: string
}>()

const emit = defineEmits(['update:modelValue'])

const allergiesOptions= [
{'id':'','value':'Ninguno'},    
{'id':'alder_pollen','value':'Aliso'},
{'id':'birch_pollen','value':'Abedul'},
{'id':'grass_pollen','value':'Gramíneas'},
{'id':'mugwort_pollen','value':'Artemisa'},
{'id':'olive_pollen','value':'Olivos'},
{'id':'ragweed_pollen','value':'Ambrosía'}]

</script>

<template>
  <select
    :value="modelValue"
    @change="emit('update:modelValue', $event.target.value)"
  >
    <option
      v-for="option in allergiesOptions"
      :key="option.id"
      :value="option.id"
    >
      {{ option.value }}
    </option>
  </select>
</template>


