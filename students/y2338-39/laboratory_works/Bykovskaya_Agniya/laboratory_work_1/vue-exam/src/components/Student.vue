<template>
<mu-container>
       <mu-appbar style="width: 100%;" color="#d7ccc8">
         <mu-menu slot="left" placement="top-start" open-on-hover>
                    <mu-button flat> Меню
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button href="#/schedule">
                            <mu-list-item-title>Расписание экзаменов</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/student">
                            <mu-list-item-title>Список студентов</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/teacher">
                            <mu-list-item-title>Список преподавателей</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/discipline">
                            <mu-list-item-title>Список дисциплин</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/exam">
                            <mu-list-item-title>Результаты экзаменов</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
  Список студентов

  <mu-button flat slot="right" href="#/">На главную</mu-button>
       </mu-appbar>
  <mu-row>
    <mu-col align="left">
      <mu-form label-position="top">
       <mu-select v-model="form_filter.course" label="Курс">
         <mu-option value="1" label="1"></mu-option>
         <mu-option value="2" label="2"></mu-option>
         <mu-option value="3" label="3"></mu-option>
         <mu-option value="4" label="4"></mu-option>
         <mu-option value="5" label="5"></mu-option>
       </mu-select>
        <mu-button small round color="#B6CEB6" @click="Filter" class="button-wrapper">Применить фильтр</mu-button>
        <mu-button small round color="#B6CEB6" @click="FilterReset" class="button-wrapper">Сброс</mu-button>
        <br>
        <mu-form-item label-position="top" prop="input" label="Группа">
          <mu-text-field v-model="form_filter.group_number"></mu-text-field>
        </mu-form-item>
         <br/>
      </mu-form>
    </mu-col>
  </mu-row>
  <mu-row>
   <mu-col align="center">
                <table>
                  <thead>
                  <tr>
                        <th>Номер зачётной книжки</th>
                        <th>Фамилия</th>
                        <th>Имя</th>
                        <th>Отчество</th>
                        <th>Курс</th>
                        <th>Группа</th>
                    </tr>
                  </thead>
                  <tbody>
                        <tr v-for="student in listStudent" :key="student.id">
                        <td>{{student.gradebook_number}}</td>
                        <td>{{student.student_surname}}</td>
                        <td>{{student.student_name}}</td>
                        <td>{{student.middle_name_of_the_student}}</td>
                        <td>{{student.course}}</td>
                        <td>{{student.group_number}}</td>
                        </tr>
                  </tbody>
                </table>
            </mu-col>
 </mu-row>
</mu-container>
</template>

<script>
export default {
  name: "Student",
  components: {},
  data() {
    return {
      listStudent: [],
      form_filter:{
        course: '',
      },
    }
  },
  created(){
    this.loadListStudent()
    this.loadListStudentAll()
  },
  methods: {
    async loadListStudent() {
      this.listStudent= await fetch(
          `http://127.0.0.1:8000/api/v1/student/?course=${this.form_filter.course}&group_number=${this.form_filter.group_number}`
                ).then(response => response.json())
            },
    async loadListStudentAll() {
      this.listStudent = await fetch(
          `http://127.0.0.1:8000/api/v1/student/`
      ).then(response => response.json())
    },
    Filter() {
      this.loadListStudent()
            },
    FilterReset() {
      this.loadListStudentAll()
            },
  }
}
</script>

<style scoped>
.button-wrapper{
  height: 25px;
  margin: 10px;
}

</style>