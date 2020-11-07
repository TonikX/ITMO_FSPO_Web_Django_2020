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
  Результаты экзаменов

  <mu-button flat slot="right" href="#/">На главную</mu-button>
       </mu-appbar>
 <mu-row>
   <mu-col align="center">
                <table>
                  <thead>
                  <tr>
                        <th>Номер экзамена</th>
                        <th>Оценка</th>
                        <th>Дисциплина</th>
                        <th>Студент</th>
                        <th>Преподаватель</th>
                    </tr>
                  </thead>
                  <tbody>
                        <tr v-for="exam in listExam" :key="exam.id">
                        <td>{{exam.exam_id}}</td>
                        <td>{{exam.assessment}}</td>
                        <td>{{exam.discipline_discipline_code.discipline_name}}</td>
                        <td>{{exam.student_gradebook_number.student_surname}} {{exam.student_gradebook_number.student_name}}
                        {{exam.student_gradebook_number.middle_name_of_the_student}} {{exam.student_gradebook_number.course}} курс</td>
                        <td>{{exam.teacher_teacher_id.surname_of_the_teacher}} {{exam.teacher_teacher_id.teacher_name}}
                          {{exam.teacher_teacher_id.teacher_middle_name}}</td>
                        </tr>
                  </tbody>
                </table>
            </mu-col>
 </mu-row>
</mu-container>
</template>

<script>
export default {
  name: "Exam",
  components: {},
  data() {
    return {
      listExam: [],
    }
  },
  created(){
    this.loadListExam()
  },
  methods: {
    async loadListExam() {
      this.listExam = await fetch(
          `http://127.0.0.1:8000/api/v1/exam/`
      ).then(response => response.json())
    },
  }
}
</script>

<style scoped>

</style>