<template>
 <mu-container>
<mu-appbar style="width: 100%;" color="#d7ccc8" title="Создание учётной записи"></mu-appbar>
        <mu-row align="center">
            <mu-col>
                <br/>
                <br/>
                <mu-text-field v-model="username" placeholder="Username"></mu-text-field><br/>
            </mu-col>
        </mu-row >
        <mu-row align="center">
            <mu-col>
                <mu-text-field v-model="password" label="Password" type="password" ></mu-text-field><br/>
            </mu-col>
        </mu-row>
        <mu-row align="center">
            <mu-col>
                <mu-text-field v-model="password2" label="Password confirmation" type="password" ></mu-text-field><br/>
            </mu-col>
        </mu-row>
        <mu-container class="button-wrapper">
            <mu-row>
                <mu-col>
            <mu-button round color="#90a4ae" @click="passwordCheck">Зарегистрироваться</mu-button>
                </mu-col>
            </mu-row>
        </mu-container>
    </mu-container>
</template>

<script>
  import $ from 'jquery'

    export default {
        name: "Signup",
        data() {
            return {
                username: '',
                password: '',
                password2: '',
            }
        },
        methods: {
            passwordCheck() {
                if (this.password === this.password2) {
                    this.signUp()
                } else {
                    alert('Passwords do not match')
                }
            },
            signUp() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/users/create/",
                    type: "POST",
                    data: {
                        username: this.username,
                        password: this.password
                    },
                    success: (response) => {
                        alert("Регистрация прошла успешно")
                        this.$router.push({name: "Login"})
                    },
                    error: (response) => {
                            if (response.status === 404) {
                                alert("Пожалуйста, проверьте корректность введённых данных")
                            }
                        }
                })
            },
        }
    }
</script>

<style scoped>

</style>