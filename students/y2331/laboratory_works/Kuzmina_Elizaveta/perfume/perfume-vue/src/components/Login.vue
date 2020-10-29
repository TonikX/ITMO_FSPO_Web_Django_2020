<template>
  <div>
    <mu-appbar style="width: 100%;text-align: center" color="deepPurple500">
      Вход в систему
      <mu-button flat slot="left" @click="mainWindow">
        <mu-icon value="home"></mu-icon>
      </mu-button>
    </mu-appbar>
    <mu-container style="text-align: center">
      <mu-form ref="form" :model="validateForm" style="padding: 100px">
        <mu-form-item label="Логин" help-text="Введите имя пользователя" prop="username" :rules="usernameRules">
          <mu-text-field v-model="validateForm.username" prop="username"></mu-text-field>
        </mu-form-item>
        <mu-form-item label="Пароль" help-text="Введите пароль" prop="password" :rules="passwordRules">
          <mu-text-field v-model="validateForm.password" prop="password"
                         :action-icon="visibility ? 'visibility_off' : 'visibility'"
                         :action-click="() => (this.visibility = !visibility)"
                         :type="visibility ? 'text' : 'password'"></mu-text-field>
        </mu-form-item>
        <mu-form-item style="align-items: center">
          <mu-button color="deepPurple500" @click="setLogin">Войти</mu-button>
          <mu-button @click="clear">Сбросить</mu-button>
        </mu-form-item>
      </mu-form>
    </mu-container>
  </div>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        validateForm: {
          username: '',
          password: '',
        },
        visibility: false,
        usernameRules: [
          {validate: (val) => !!val, message: 'Имя пользователя должно быть заполнено'},
        ],
        passwordRules: [
          {validate: (val) => !!val, message: 'Пароль должен быть заполнен'},
        ],
      }
    },
    methods: {
      setLogin() {
        this.$refs.form.validate().then((result) => {
          if (result === false) {
            alert('Какие-то поля заполнены неверно.');
          } else {
            $.ajax({
              url: "http://127.0.0.1:8000/auth/token/login/",
              type: "POST",
              data: {
                username: this.validateForm.username,
                password: this.validateForm.password,
              },
              success: (response) => {
                alert("Вход в систему");
                localStorage.setItem("auth_token", response.data.attributes.auth_token);
                this.$router.push({name: "home"})
              },
              error: (response) => {
                if (response.status === 400) {
                  alert("Неправильный логин или пароль")
                }
              }
            })
          }
        })
      },
      clear() {
        this.$refs.form.clear();
        this.validateForm = {
          username: '',
          password: '',
        };
      },
      mainWindow() {
        this.$router.push({name: "home"})
      },
    }
  }
</script>

<style scoped>
  .mu-demo-form {
    width: 100%;
    max-width: 460px;
  }
</style>
