<script setup lang="ts">

</script>

<template>
  <form class="form">        
        <label for="name">Nombre y apellidos</label>
        <input type="text" name="name">
        <label for="birth-date">Fecha de nacimiento</label>
        <input type="text" name="birth-date">
        <label for="location">Ciudad de residencia</label>
        <input type="text" name="location">
        <label for="allergies">Alergias conocidas</label>
        <input type="text" name="allergies">
        <label for="email">Correo electrónico</label>
        <input type="text" name="email">
        <label for="password">Crear contraseña</label>
        <input type="password" name="password">
        <button class="button">Crear usuario</button>        
  </form>
</template>
<style>
    .form{        
        max-width: 30%;
        display: flex;
        flex-direction: column;
        padding: 2em;
    }
    .form label{
        padding-top: 1em;
    }
    .button{
        margin-top: 2em;
        max-width: 40%;

    }
</style>