<template>
  <div>
    <mu-appbar style="width: 100%;text-align: center" color="deepPurple500">
      Парфюмерный базар
      <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
      <mu-button flat slot="right" v-else @click="logout">Выход</mu-button>
    </mu-appbar>
    <mu-container>
      <mu-row>
        <Menu v-if="auth"></Menu>
      </mu-row>
      <mu-row>
        <mu-card v-if="!auth" style="width: 100%;text-align: center;margin: 100px">
          <mu-card-title title="Для дальнейшего взаимодействия войдите в профиль..."></mu-card-title>
        </mu-card>
      </mu-row>
    </mu-container>
  </div>
</template>

<script>
  import Menu from '@/components/Menu';

  export default {
    name: "Home",
    components: {
      Menu
    },
    computed: {
      auth() {
        if (localStorage.getItem("auth_token")) {
          return true
        }
      }
    },
    methods: {
      goLogin() {
        this.$router.push({name: "login"})
      },
      logout() {
        localStorage.removeItem("auth_token");
        window.location = '/'
      },
    }
  }
</script>

<style scoped>

</style>
