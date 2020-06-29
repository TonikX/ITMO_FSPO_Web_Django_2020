<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="indigo400">
            Автобусы
            <mu-button flat slot="right" @click="goHome">Главная</mu-button>
            <mu-button flat slot="left" v-if="auth" @click="openEditDialog()">Добавить</mu-button>
        </mu-appbar>
        <mu-paper :z-depth="1" align="center">
            <mu-data-table :columns="columns" :data="buses">
                <template slot-scope="scope" align="center">
                    <td>{{scope.row.busName}}</td>
                    <td>{{scope.row.mileage}}</td>
                    <td>{{scope.row.busType}}</td>
                    <td>{{scope.row.busNumber}}</td>
                </template>
            </mu-data-table>
        </mu-paper>
        <mu-container aligh="left">
            <mu-dialog title="Добавить" width="500" :open.sync="openEdit">
                <mu-text-field v-model="editForm.busName" type="text" placeholder="Название"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.mileage" type="text" placeholder="Пробег"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.busType" type="text" placeholder="Тип прав"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.busNumber" type="text" placeholder="Номер автобуса"></mu-text-field>
                <br>
                <!--                <mu-button slot="actions" color="green" @click="updateBus()">Сохранить</mu-button>-->
                <mu-button slot="actions" color="amber300" @click="addBus()">Добавить</mu-button>
                <!--                <mu-button slot="actions" color="red" @click="deleteBus()">Удалить</mu-button>-->
                <mu-button slot="actions" color="primary" @click="closeEditDialog">Закрыть</mu-button>
            </mu-dialog>
        </mu-container>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Bus",
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
                buses: '',
                columns: [
                    {title: 'Название', name: 'busName', sortable: false},
                    {title: 'Пробег', name: 'mileage', sortable: false},
                    {title: 'Тип прав', name: 'busType', sortable: false},
                    {title: 'Номер автобуса', name: 'busNumber', sortable: false}
                ],
                editForm: {
                    busName: '',
                    mileage: '',
                    busType: '',
                    busNumber: ''
                },
                openEdit: false
            }
        },
        created() {
            this.loadBuses()
        },
        methods: {
            loadBuses() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/bus/",
                    type: "GET",
                    success: (response) => {
                        this.buses = response.data.data
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Home"})
            },
            openEditDialog(busName, mileage, busType, busNumber) {
                this.editForm.busName = busName
                this.editForm.mileage = mileage
                this.editForm.busType = busType
                this.editForm.busNumber = busNumber
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            addBus() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/bus/",
                    type: "POST",
                    data: {
                        busName: this.editForm.busName,
                        mileage: this.editForm.mileage,
                        busType: this.editForm.busType,
                        busNumber: this.editForm.busNumber
                    },
                    success: (response) => {
                        alert("Автобус добавлен")
                        this.loadBuses()
                        this.editForm = {
                            busName: '',
                            mileage: '',
                            busType: '',
                            busNumber: ''
                        };
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
