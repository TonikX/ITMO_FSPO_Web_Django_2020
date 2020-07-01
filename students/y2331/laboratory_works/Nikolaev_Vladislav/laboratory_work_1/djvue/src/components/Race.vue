<!--Выполненные рейсы-->
<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="secondary">
            Рейсы
            <mu-button flat slot="right" @click="goHome">Главная</mu-button>
            <mu-button flat slot="left" v-if="auth" @click="openEditDialog">Статистика</mu-button>
        </mu-appbar>
        <mu-paper :z-depth="1" align="center">
            <mu-data-table :columns="columns" :data="races">
                <template slot-scope="scope" align="center">
                    <td>{{scope.row.dateStart}}</td>
                    <td>{{scope.row.dateFinish}}</td>
                    <td>{{scope.row.amount}}</td>
                    <td>{{scope.row.price}}₽</td>
                    <td>{{scope.row.state}}</td>
                    <td>{{scope.row.raceRoute.routeName}}</td>
                    <td>{{scope.row.raceBus.busNumber}}</td>
                </template>
            </mu-data-table>
        </mu-paper>
        <mu-container aligh="left">
            <mu-dialog title="Статистика" width="500" :open.sync="openEdit">
                Общее количество записей: {{this.rows}}
                <br>
                Средняя цена билета: {{this.middlePrice}}₽
                <br>
                Среднее количество пассажиров: {{this.middlePassangers}}
                <mu-button slot="actions" color="primary" @click="closeEditDialog">Закрыть</mu-button>
            </mu-dialog>
        </mu-container>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Profile",
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
                races: '',
                rows: '',
                middlePrice: '',
                middlePassangers: '',
                columns: [
                    {title: 'Дата отправления', name: 'dateStart', sortable: false},
                    {title: 'Дата прибытия', name: 'dateFinish', sortable: false},
                    {title: 'Количество пассажиров', name: 'amount', sortable: false, width: 200},
                    {title: 'Цена билета', name: 'price', sortable: false},
                    {title: 'Состояние', name: 'state', sortable: false},
                    {title: 'Маршрут отправки', name: 'raceRoute', sortable: false, width: 200},
                    {title: 'Автобус маршрута', name: 'raceBus', sortable: false}
                ],
                openEdit: false
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadRaces()
        },
        methods: {
            loadRaces() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/race/",
                    type: "GET",
                    success: (response) => {
                        this.races = response.data.data;
                        let boofPrice = 0.00;
                        let boofPassangers = 0;
                        for (let i = 0; i < this.races.length; i++) {
                            boofPrice += parseFloat(response.data.data[i].price);
                            boofPassangers += parseInt(response.data.data[i].amount)
                        }
                        boofPrice = boofPrice / this.races.length;
                        this.middlePrice = boofPrice;
                        boofPassangers = parseInt(boofPassangers / this.races.length);
                        this.middlePassangers = boofPassangers;
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Home"})
            },
            openEditDialog() {
                this.rows = this.races.length;
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            }
        }
    }
</script>

<style scoped>

</style>
