<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="primary">
            <div align="center">Экскурсии</div>
            <mu-button flat slot="right" v-if="!auth" @click="goLogin">Вход</mu-button>
            <mu-button flat slot="right" v-if="auth" @click="goLogout">Выход</mu-button>
            <mu-button flat slot="left" v-if="auth" @click="goProfiles">Сотрудники</mu-button>
        </mu-appbar>
        <mu-row>
            <h1>Навигация</h1>
        </mu-row>
        <mu-grid-list cols="2" cell-height="250" padding="10">
            <mu-grid-tile button @click="goBuses" title="Автобусы" sub-title="Посмотреть автопарк" class="fade">
                <img src="../assets/bus.jpg">
            </mu-grid-tile>
            <mu-grid-tile button @click="goRoutes" title="Маршруты" sub-title="Посмотреть экскурсии" class="fade">
                <img src="../assets/route.png">
            </mu-grid-tile>
            <mu-grid-tile button v-if="auth" @click="goDrivers" title="Водители" sub-title="Посмотреть информацию о водителях" class="fade">
                <img src="../assets/driver.jpg">
            </mu-grid-tile>
            <mu-grid-tile button v-if="auth" @click="goRaces" title="Рейсы" sub-title="Посмотреть выполненные рейсы" class="fade">
                <img src="../assets/race.jpg">
            </mu-grid-tile>
        </mu-grid-list>
    </mu-container>
</template>

<script>
    export default {
        name: "Home",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Login"})
            },
            goLogout() {
                sessionStorage.removeItem("auth_token")
                window.location = '/'
            },
            goBuses() {
                this.$router.push({name: "Bus"})
            },
            goRaces() {
                this.$router.push({name: "Race"})
            },
            goProfiles() {
                this.$router.push({name: "Profile"})
            },
            goRoutes() {
                this.$router.push({name: "Route"})
            },
            goDrivers() {
                this.$router.push({name: "Drivers"})
            }
        }
    }
</script>

<style scoped>
    .fade {
        opacity: 1;
        transition: 0.3s;
    }

    .fade:hover {
        opacity: 0.6;
        transition: 0.3s;
    }
</style>
