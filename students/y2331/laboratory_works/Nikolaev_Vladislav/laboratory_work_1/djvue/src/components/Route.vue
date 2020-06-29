<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="deepOrange300">
            <div align="center">Маршруты</div>
            <mu-button flat slot="right" @click="goHome">Главная</mu-button>
            <mu-button flat slot="left" v-if="auth" @click="openEditDialog()">Добавить</mu-button>
        </mu-appbar>
        <mu-paper :z-depth="1" align="center">
            <mu-data-table :columns="columns" :data="routes">
                <template slot-scope="scope" align="center">
                    <td>{{scope.row.routeName}}</td>
                    <td>{{scope.row.startCity}}</td>
                    <td>{{scope.row.finishCity}}</td>
                    <td>{{scope.row.distance}}км</td>
                </template>
            </mu-data-table>
        </mu-paper>
        <mu-container aligh="left">
            <mu-dialog title="Добавить" width="500" :open.sync="openEdit">
                <mu-text-field v-model="editForm.routeName" type="text" placeholder="Название"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.startCity" type="text" placeholder="Город отправления"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.finishCity" type="text" placeholder="Город прибытия"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.distance" type="text" placeholder="Протяженность маршрута"></mu-text-field>
                <br>
<!--                <mu-button slot="actions" color="green" @click="updateRoute()">Сохранить</mu-button>-->
                <mu-button slot="actions" color="amber300" @click="addRoute()">Добавить</mu-button>
<!--                <mu-button slot="actions" color="red" @click="deleteRoute()">Удалить</mu-button>-->
                <mu-button slot="actions" color="primary" @click="closeEditDialog">Закрыть</mu-button>
            </mu-dialog>
        </mu-container>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Route",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    $.ajaxSetup({
                        headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
                    });
                    return true
                }
            }
        },
        data() {
            return {
                routes: '',
                columns: [
                    {title: 'Название', name: 'routeName', sortable: false},
                    {title: 'Город отправления', name: 'startCity', sortable: false},
                    {title: 'Город прибытия', name: 'finishCity', sortable: false},
                    {title: 'Протяженность маршрута', name: 'distance', sortable: false}
                ],
                editForm: {
                    routeName: '',
                    startCity: '',
                    finishCity: '',
                    distance: ''
                },
                openEdit: false
            }
        },
        created() {
            this.loadRoutes()
        },
        methods: {
            loadRoutes() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/route/",
                    type: "GET",
                    success: (response) => {
                        this.routes = response.data.data
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Home"})
            },
            openEditDialog(routeName, startCity, finishCity, distance) {
                this.editForm.routeName = routeName
                this.editForm.startCity = startCity
                this.editForm.finishCity = finishCity
                this.editForm.distance = distance
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            addRoute() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/route/",
                    type: "POST",
                    data: {
                        routeName: this.editForm.routeName,
                        startCity: this.editForm.startCity,
                        finishCity: this.editForm.finishCity,
                        distance: this.editForm.distance
                    },
                    success: (response) => {
                        alert("Маршрут добавлен")
                        this.loadRoutes()
                        this.editForm = {
                            routeName: '',
                            startCity: '',
                            finishCity: '',
                            distance: ''
                        };
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            updateRoute() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/route/",
                    type: "PUT",
                    data: {
                        routeName: this.editForm.routeName,
                        startCity: this.editForm.startCity,
                        finishCity: this.editForm.finishCity,
                        distance: this.editForm.distance
                    },
                    success: (response) => {
                        alert("Маршрут обновлен")
                        this.loadRoutes()
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            deleteRoute() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/route/",
                    type: "DELETE",
                    success: (response) => {
                        alert("Маршрут удален")
                        this.loadRoutes()
                        this.closeEditDialog()
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
