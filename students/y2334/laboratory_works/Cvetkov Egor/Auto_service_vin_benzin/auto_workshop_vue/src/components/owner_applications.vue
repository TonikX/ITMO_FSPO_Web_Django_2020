<template>
    <mu-container>
    <vue-headful title="Мои заявки"/>
        <mu-row>
            <mu-appbar style="width: 100%; background: rgb(1,1,4);
                background: linear-gradient(90deg, rgba(1,1,4,1) 0%, rgba(235,235,235,0.3925945378151261) 100%);">
                <span class="main-font" style="font-size: 20pt; float: left;color: white">Сеть автомастерских &laquoВин-Бенз&raquo</span>
                <mu-button flat slot="right" @click="goto_main">На главную</mu-button>
            </mu-appbar>
        </mu-row>
        <mu-row>
            <h1 class="main-font">Мои заявки</h1>
        </mu-row>


        <mu-row class="alert" v-if="alert">
            <mu-col span=10>
                <span class="main-font" style="font-size: 18pt; float: left">{{alert_text}}</span>
            </mu-col>
            <mu-col span=2>
                <mu-button class="blue-button" @click="close_alert">Ок</mu-button>
            </mu-col>
        </mu-row>

        <mu-row gutter v-for="application in applications">
        <div class="info-pannel" style="width: 70%">
            <mu-row>
                <mu-col span=8>
                    <span class="main-font" style="font-size: 20pt; float: left">Мастерская №{{application.workshop.number}}</span>
                </mu-col>
                <mu-col span=4>
                    <span class="main-font" style="font-size: 20pt; float: right">{{application.date_init}}</span>
                </mu-col>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 20pt; text-align: left">{{application.auto.brand}} {{application.auto.model}} {{application.auto.number}}</span>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 15pt; text-align: left">Статус: {{application.status}}</span>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 15pt; text-align: left">Дата записи: {{application.date}}</span>
            </mu-row>
            <mu-row>
                <span class="main-font" style="font-size: 15pt; text-align: left">Описание: {{application.description}}</span>
            </mu-row>
            <div v-if="status_check(application)" style="margin: 5% auto 0">
                <mu-button class="red-button" @click="open_delete_dialog">Отозвать</mu-button>
       <mu-button class="green-button" @click="goto_application_add">Добавить заявку</mu-button>
                <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="delete_dialog">
                    <span class="main-font" style="font-size: 18pt; margin: 0 auto; color: #212121">Вы точно уверены, что хотите отозвать заявку?</span>
                    <div align="center" style="margin-top: 5%">
                        <mu-button class="blue-button" slot="actions" @click="close_delete_dialog">Отмена</mu-button>
                        <mu-button class="red-button" slot="actions" @click="conf_delete(application.id)">Отозвать</mu-button>

                    </div>
                </mu-dialog>

            </div>
        </div>
        </mu-row>

        <mu-dialog width="50%" :esc-press-close="false" :overlay-close="false" :open.sync="alert_dialog">
            <span class="main-font" style="font-size: 18pt; margin: 0 auto; color: white">{{alert_text}}</span>
            <div align="center" style="margin-top: 5%">
                <mu-button class="blue-button" slot="actions" @click="close_alert_dialog">Ок</mu-button>
            </div>
        </mu-dialog>

    </mu-container>
</template>


<script>
    import $ from 'jquery'

    export default {
        name: "Owner_applications",
        data() {
            return {
                applications: "",
                delete_dialog: false,
                alert_dialog: false,
                alert: false,
                alert_text: "",
            }
        },
        created() {
            $.ajaxSetup({
                headers: {"Authorization": "Token " + sessionStorage.getItem("auth_token")}
            });
            this.get_applications()
            if(this.$route.query.outer_alert) {
                this.alert_text = this.$route.query.outer_alert;
                this.show_alert()
            }
        },
        methods: {
            goto_main() {
                this.$router.push({name: "main_rout"})
            },
            goto_application_add() {
                this.$router.push({name: "owner_application_add_rout"})
            },
            get_applications() {
                $.ajax({
                    url: "http://127.0.0.1:8000/owner_applications_list/",
                    type: "GET",
                    success: (response) => {
                        this.applications = response.data.data
                    },
                    error: (response) => {
                        this.alert_text = "Ошибка на стороне сервера";
                        this.open_alert_dialog()
                    }
                })
            },
            open_delete_dialog() {
                this.delete_dialog = true;
            },
            close_delete_dialog() {
                this.delete_dialog = false;
            },
            status_check(application) {
                if(application.status=="Подтверждено") {
                    return false
                }
                return true
            },
            remove_application(id) {
                var href = "http://127.0.0.1:8000/owner_application_remove/" + id + "/"
                $.ajax({
                    url: href,
                    type: "DELETE",
                    success: (response) => {
                        this.alert_text = "Заявка возвращена";
                        this.show_alert()
                        this.get_applications()
                        this.$forceUpdate();
                    },
                    error: (response) => {
                        this.alert_text = "Ошибка на стороне сервера";
                        this.open_alert_dialog()
                    }
                })
            },
            conf_delete(id) {
                this.close_delete_dialog()
                this.remove_application(id)
            },
            open_alert_dialog() {
                this.alert_dialog = true;
            },
            close_alert_dialog() {
                this.alert_dialog = false;
            },
            show_alert() {
                this.alert = true;
            },
            close_alert() {
                this.alert = false;
            }
        },
    }
</script>


<style lang="scss" scoped>
    @import '@/assets/styles.scss';
</style>
