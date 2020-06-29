<template>
    <mu-container>
        <mu-appbar style="width: 100%;" color="teal300">
            Сотрудники
            <mu-button flat slot="right" @click="goHome">Главная</mu-button>
<!--            <mu-button flat slot="left" v-if="auth" @click="openEditDialog()">Добавить</mu-button>-->
        </mu-appbar>
        <mu-paper :z-depth="1" align="center">
            <mu-data-table :columns="columns" :data="profiles">
                <template slot-scope="scope" align="center">
                    <td>{{scope.row.user.username}}</td>
                    <td>{{scope.row.fullName}}</td>
                    <td>{{scope.row.birth_date}}</td>
                    <td>{{scope.row.position}}</td>
                    <td>{{scope.row.location}}</td>
                    <td>{{scope.row.contacts}}</td>
                </template>
            </mu-data-table>
        </mu-paper>
        <mu-container aligh="left">
            <mu-dialog title="Добавить" width="500" :open.sync="openEdit">
                <mu-text-field v-model="editForm.username" type="text" placeholder="Имя пользователя"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.fullName" type="text" placeholder="ФИО"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.birth_date" type="text" placeholder="Дата регистрации"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.position" type="text" placeholder="Должность"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.location" type="text" placeholder="Адрес"></mu-text-field>
                <br>
                <mu-text-field v-model="editForm.contacts" type="text" placeholder="Контакты"></mu-text-field>
                <br>
<!--                <mu-button slot="actions" color="green" @click="updateRoute()">Сохранить</mu-button>-->
                <mu-button slot="actions" color="amber300" @click="addProfile()">Добавить</mu-button>
<!--                <mu-button slot="actions" color="red" @click="deleteRoute()">Удалить</mu-button>-->
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
                profiles: '',
                columns: [
                    {title: 'Никнейм', name: 'username', sortable: false, width: 150},
                    {title: 'ФИО', name: 'fullName', sortable: false},
                    {title: 'Дата регистрации', name: 'birth_date', sortable: false},
                    {title: 'Должность', name: 'position', sortable: false},
                    {title: 'Адрес', name: 'location', sortable: false},
                    {title: 'Контакты', name: 'contacts', sortable: false}
                ],
                editForm: {
                    username: '',
                    fullName: '',
                    birth_date: '',
                    position: '',
                    location: '',
                    contacts: ''
                },
                openEdit: false
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadProfiles()
        },
        methods: {
            loadProfiles() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/profile/",
                    type: "GET",
                    success: (response) => {
                        this.profiles = response.data.data
                    }
                })
            },
            goHome() {
                this.$router.push({name: "Home"})
            },
            openEditDialog(user, fullName, birth_date, position, location) {
                this.editForm.user = user
                this.editForm.fullName = fullName
                this.editForm.birth_date = birth_date
                this.editForm.position = position
                this.editForm.location = location
                this.editForm.contacts = contacts
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            addProfile() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/profile/",
                    type: "POST",
                    data: {
                        user: this.editForm.user,
                        fullName: this.editForm.fullName,
                        birth_date: this.editForm.birth_date,
                        position: this.editForm.position,
                        location: this.editForm.location,
                        contacts: this.editForm.contacts
                    },
                    success: (response) => {
                        alert("Клиент добавлен")
                        this.loadProfiles()
                        this.editForm = {
                            user: '',
                            fullName: '',
                            birth_date: '',
                            position: '',
                            location: '',
                            contacts: ''
                        };
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            updateProfile() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/profile/",
                    type: "PUT",
                    data: {
                        user: this.editForm.user,
                        fullName: this.editForm.fullName,
                        birth_date: this.editForm.birth_date,
                        position: this.editForm.position,
                        location: this.editForm.location,
                        contacts: this.editForm.contacts
                    },
                    success: (response) => {
                        alert("Клиент обновлен")
                        this.loadProfiles()
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Ошибка")
                    }
                })
            },
            deleteProfile() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/djlab/profile/",
                    type: "DELETE",
                    success: (response) => {
                        alert("Клиент удален")
                        this.loadProfiles()
                        this.closeEditDialog()
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>
