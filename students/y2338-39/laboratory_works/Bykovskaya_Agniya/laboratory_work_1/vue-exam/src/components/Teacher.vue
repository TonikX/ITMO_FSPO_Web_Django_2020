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
  Список преподавателей

  <mu-button flat slot="right" href="#/">На главную</mu-button>
       </mu-appbar>
  <mu-row>
    <mu-col align="left">
      <mu-form label-position="top">
        <br>
        <mu-form-item label-position="top" prop="input" label="Кафедра">
          <mu-text-field v-model="form_filter.department"></mu-text-field>
        </mu-form-item>
        <mu-button small round color="#B6CEB6" @click="Filter" class="button-wrapper">Применить фильтр</mu-button>
        <mu-button small round color="#B6CEB6" @click="FilterReset" class="button-wrapper">Сброс</mu-button>
         <br/>
      </mu-form>
    </mu-col>
  </mu-row>
 <mu-row>
            <mu-col align="center">
                <table>
                  <thead>
                  <tr>
                        <th>ID преподавателя</th>
                        <th>Фамилия</th>
                        <th>Имя</th>
                        <th>Отчество</th>
                        <th>Кафедра</th>
                    </tr>
                  </thead>
                  <tbody>
                        <tr v-for="teacher in listTeacher" :key="teacher.id">
                        <td>{{teacher.teacher_id}}</td>
                        <td>{{teacher.surname_of_the_teacher}}</td>
                        <td>{{teacher.teacher_name}}</td>
                        <td>{{teacher.teacher_middle_name}}</td>
                        <td>{{teacher.department}}</td>
                        </tr>
                  </tbody>
                </table>
            </mu-col>
 </mu-row>
</mu-container>
</template>

<script>
export default {
  name: "Teacher",
  components: {},
  data() {
    return {
      listTeacher: [],
      form_filter:{
        department: '',
      },
    }
  },
  created(){
    this.loadListTeacher()
    this.loadListTeacherAll()
  },
  methods: {
    async loadListTeacherAll() {
      this.listTeacher = await fetch(
          `http://127.0.0.1:8000/api/v1/teacher/`
      ).then(response => response.json())
    },
     async loadListTeacher() {
      this.listTeacher  = await fetch(
          `http://127.0.0.1:8000/api/v1/teacher/?department=${this.form_filter.department}`
                ).then(response => response.json())
            },
    Filter() {
      this.loadListTeacher()
            },
    FilterReset() {
      this.loadListTeacherAll()
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