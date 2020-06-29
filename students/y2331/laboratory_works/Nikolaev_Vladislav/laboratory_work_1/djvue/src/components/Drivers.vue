<template>
    <mu-container>
    <mu-appbar style="width: 100%;" color="blueA200">
      Водители
      <mu-button flat slot="right" @click="goHome">Главная</mu-button>
<!--        <mu-button flat slot="left" v-if="auth" @click="openEditDialog()">Добавить</mu-button>-->
    </mu-appbar>
    <mu-paper :z-depth="1" align="center">
      <mu-data-table :columns="columns" :data="drivers">
        <template slot-scope="scope" align="center">
          <td>{{scope.row.person.fullName}}</td>
          <td>{{scope.row.experience}}</td>
          <td>{{scope.row.category}}</td>
          <td>{{scope.row.driverBus.busNumber}}</td>
        </template>
      </mu-data-table>
    </mu-paper>
        <mu-container aligh="left">
            <mu-dialog title="Добавить" width="500" :open.sync="openEdit">
                <mu-text-field v-model="editForm.person.fullName" type="text" placeholder="Название"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.experience" type="text" placeholder="Пробег"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.category" type="text" placeholder="Тип прав"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.driverBus.busNumber" type="text" placeholder="Номер автобуса"></mu-text-field>
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
        name: "Profile",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        data() {
            return {
                drivers: '',
                columns: [
                    {title: 'Гражданин', name: 'person', sortable: false},
                    {title: 'Стаж вождения', name: 'experience', sortable: false},
                    {title: 'Категория прав', name: 'category', sortable: false},
                    {title: 'Автобус водителя', name: 'driverBus', sortable: false}
                ],
                editForm: {
                    person: '',
                    experience: '',
                    category: '',
                    driverBus: ''
                },
                openEdit: false
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadDrivers()
        },
        methods: {
            loadDrivers() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/drivers/",
                    type: "GET",
                    success: (response) => {
                        this.drivers = response.data.data
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Home"})
            },
            openEditDialog(person, experience, category, driverBus) {
                this.editForm.person = person
                this.editForm.experience = experience
                this.editForm.category = category
                this.editForm.driverBus = driverBus
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
                        person: this.editForm.person,
                        experience: this.editForm.experience,
                        category: this.editForm.category,
                        driverBus: this.editForm.driverBus
                    },
                    success: (response) => {
                        alert("Клиент добавлен")
                        this.loadBuses()
                        this.editForm = {
                            person: '',
                            experience: '',
                            category: '',
                            driverBus: ''
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
