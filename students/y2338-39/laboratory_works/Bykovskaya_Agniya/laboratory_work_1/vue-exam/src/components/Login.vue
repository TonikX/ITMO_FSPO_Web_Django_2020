<template>
  <mu-container>
     <mu-appbar style="width: 100%;" color="#d7ccc8" title="Вход"></mu-appbar>
        <mu-row align="center">
            <mu-col>
                <br>
                <br>
                <mu-text-field v-model="login" label="Имя пользователя" label-float
                               help-text=""></mu-text-field>
                <br/>
                <mu-text-field v-model="password" label="Пароль" type="password" label-float
                               error-text=""></mu-text-field>
                <br/>
                <mu-button round color="#90a4ae" @click="setLogin">Войти</mu-button>
            </mu-col>
        </mu-row>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
    name: "Login",
         data() {
             return {
                login: '',
                password: '',
             }
         },
        methods: {
            setLogin(){
                $.ajax({
                  url: "http://127.0.0.1:8000/auth/token/create/",
                  type: "POST",
                  data: {
                    username: this.login,
                    password: this.password
                  },
                  success: (response) => {
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        alert("Добро пожаловать!")
                        this.$router.push({name: "ExamSchedule"})
                    },
                    error: (response) => {
                        if (response.status === 404) {
                            alert("Неверное имя пользователя или пароль")
                        }
                  }
                })
            },
        }
  }
</script>

<style scoped>

</style>