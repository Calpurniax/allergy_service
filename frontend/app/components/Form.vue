<script setup lang="ts">
import Select from './Select.vue'

const apiUser='http://127.0.0.1:8000/api/user/'
const apiEmail ='http://127.0.0.1:8000/api/send-email/'

const formData = reactive({
  name: '',
  email: '',
  birthdate: '',
  location: '',
  allergies: '',
  password: ''
})

async function submitHandler (event: Event) {
  event.preventDefault()
  console.log(formData) 
  try{
    const res = await $fetch.raw(apiUser, {
    ignoreResponseError: true,
    method: 'POST',
    body: JSON.stringify(formData) 
  })
  console.log(res)
  if(res.status === 201){
    try{
      const res = await $fetch(apiEmail,{
        method:'POST',
        body: JSON.stringify(formData),
      })
    }catch(e){console.log(e)}
  }
  }catch(e){
    console.log(e)
  }
  
}



</script>

<template>
  <form class="form">
    <label for="name">Nombre y apellidos</label>
    <input type="text" name="name" v-model="formData.name">
    <label for="birthdate">Fecha de nacimiento</label>
    <input type="text" name="birthdate" v-model="formData.birthdate">
    <label for="location">Ciudad de residencia</label>
    <input type="text" name="location" v-model="formData.location">
    <label for="allergies">Alergia</label>
    <Select v-model="formData.allergies">  </Select>
    <label for="email">Correo electrónico</label>
    <input type="text" name="email" v-model="formData.email">   
    <label for="password">Crear contraseña</label>    
    <input type="password" name="password" v-model="formData.password">
    <button class="button" @click="submitHandler">Crear usuario</button>
  </form>
</template>


<style>
.form {
  max-width: 30%;
  display: flex;
  flex-direction: column;
  padding: 2em;
}

.form label {
  padding-top: 1em;
}

.button {
  margin-top: 2em;
  max-width: 40%;

}
</style>