<script setup lang="ts">

const formData = reactive({
  name: '',
  email: '',
  birthdate: '',
  location: '',
  allergies: '',
  password: ''
})

function submitHandler (event: Event) {
  event.preventDefault()
  console.log(formData)
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
    <label for="allergies">Alergias conocidas</label>
    <input type="text" name="allergies" v-model="formData.allergies">
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