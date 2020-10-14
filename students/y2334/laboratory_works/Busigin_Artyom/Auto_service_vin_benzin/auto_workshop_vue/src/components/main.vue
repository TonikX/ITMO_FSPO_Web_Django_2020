<template >
    <mu-container>
    <vue-headful title='Сеть автомастерских "Работает_и_славно"'/>
        <mu-row>

            <mu-appbar style="width: 100%; background: rgb(1,1,4);
                background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(25,255,0,1) 76%, rgba(0,212,255,1) 100%);">
                <span class="main-font" style="font-size: 20pt; float: left; color:white;">Сеть автомастерских &laquoРаботает_и_славно&raquo</span>
                <mu-button flat slot="right" @click="goto_owner_autos">Мои авто</mu-button>
                <mu-button flat slot="right" @click="goto_owner_applications">Мои заявки</mu-button>
                <mu-button flat slot="right" v-if="!auth" @click="goto_login">Войти</mu-button>
                <mu-button flat slot="right" v-if="!auth" @click="goto_owner_registration">Регистрация</mu-button>
                <mu-button flat slot="right" v-else @click="logout">Выйти</mu-button>
            </mu-appbar>
        </mu-row>

        <Workshops @send_alert="catch_alert"/>

        <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="alert_dialog">
            <span class="main-font" style="font-size: 10pt; margin-left;100px; color: #212121;">{{alert_text}}</span>
            <div align="center" style="margin-top: 3%" color="while">
                <mu-button class="blue-button" slot="actions" @click="close_alert_dialog">Ок</mu-button>
            </div>
        </mu-dialog>

    </mu-container>
</template>


<script>
    import $ from 'jquery'
    import Workshops from '@/components/workshops'

    export default {
        name: "Main",
        components: {
            Workshops
        },
        data() {
            return {
                alert_dialog: false,
                alert_text: "",
            }
        },
        computed: {
            auth() {
                if(sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
        	goto_login() {
        		this.$router.push({name: "login_rout"})
        	},
            goto_owner_registration() {
                this.$router.push({name: "owner_registration_rout"})
            },
            logout() {
                sessionStorage.removeItem("auth_token")
                window.location = "/"
            },
            goto_owner_autos() {
                if(sessionStorage.getItem("auth_token")) {
                    this.$router.push({name: "owner_autos_rout"})
                }
                else {
                    this.$router.push({name: "login_rout"})

                }
            },
            goto_owner_applications() {
                if(sessionStorage.getItem("auth_token")) {
                    this.$router.push({name: "owner_applications_rout"})
                }
                else {
                    this.$router.push({name: "login_rout"})

                }
            },
            catch_alert(alert_text) {
                this.alert_text = alert_text
                this.open_alert_dialog()
            },
            open_alert_dialog() {
                this.alert_dialog = true;
            },
            close_alert_dialog() {
                this.alert_dialog = false;
            },
        },
    }
</script>


<style lang="scss" scoped>
    @import '@/assets/styles.scss';
</style>
