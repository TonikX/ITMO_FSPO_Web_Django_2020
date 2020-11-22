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
  Расписание экзаменов

  <mu-button flat slot="right" href="#/">На главную</mu-button>
       </mu-appbar>
 <mu-row>
            <mu-col align="center">
                <table>
                  <thead>
                  <tr>
                    <th>Номер экзамена</th>
                    <th>Дата экзамена</th>
                    <th>Аудитория</th>
                    <th>Группа</th>
                    </tr>
                  </thead>
                  <tbody>
                        <tr v-for="exam_schedule in listExamSchedule" :key="exam_schedule.id">
                          <td>
                        <mu-radio v-if="isDeleteVisible" v-model="form_delete" :value="exam_schedule.id" label=""></mu-radio>
                            {{exam_schedule.exam_id}}
                        </td>
                        <td>{{exam_schedule.complition_date_exam}}</td>
                        <td>{{exam_schedule.the_audience}}</td>
                        <td>{{exam_schedule.group_number}}</td>
                        </tr>
                  </tbody>
                </table>
            </mu-col>
   </mu-row>
    <mu-row>
    <mu-col v-if="isCreateVisible">
      <br>
                <mu-form label-position="left">
                  <mu-form-item prop="input" label="Номер экзамена">
                        <mu-text-field v-model="form_create.exam_id"></mu-text-field>
                  </mu-form-item>
                  <mu-form-item prop="date" label="Дата экзамена">
                    <mu-text-field v-model="form_create.complition_date_exam" type="date"></mu-text-field>
                  </mu-form-item>
                  <mu-form-item prop="input" label="Аудитория">
                        <mu-text-field v-model="form_create.the_audience"></mu-text-field>
                  </mu-form-item>
                  <mu-form-item prop="input" label="Группа">
                        <mu-text-field v-model="form_create.group_number"></mu-text-field>
                  </mu-form-item>
                </mu-form>
            <br/>
                <mu-button small round color="#B6CEB6" @click="CreateExamSchedule">Добавить</mu-button>
            </mu-col>
        </mu-row>
        <mu-row>
            <mu-col v-if="isDeleteVisible">
              <mu-flex  justify-content="left" align-items="center" class="button-wrapper">
                <mu-button small round color="#B6CEB6" @click="DeleteExamSchedule">Удалить</mu-button>
                </mu-flex>
            </mu-col>
        </mu-row>
      <br>
      <mu-flex justify-content="center" align-items="center" class="button-wrapper">
        <mu-button round color="#B6CEB6" @click="goCreate">Добавить</mu-button>
        <mu-button round color="#B6CEB6" @click="goDelete">Удалить</mu-button>
      </mu-flex>
      <br/>
    </mu-container>
</template>

<script>
import $ from 'jquery'
export default {
  name: "ExamSchedule",
  components: {},
  data() {
    return {
      listExamSchedule: [],
      isCreateVisible: false,
      isDeleteVisible: false,
      form_create: {
        exam_id: '',
        complition_date_exam: '',
        the_audience: '',
        group_number: '',
      },
      form_delete: {},
    }
  },
  created() {
    this.loadListExamSchedule()
  },
  methods: {
    async loadListExamSchedule() {
      this.listExamSchedule = await fetch(
          `http://127.0.0.1:8000/api/v1/exam_schedule/`
      ).then(response => response.json())
    },
    sortByNumber(){
      this.users_data.sort((a,b) => a.complition_date_exam.localeCompare(b.complition_date_exam))
    },
    goDelete() {
                this.isDeleteVisible = !this.isDeleteVisible
            },
            async DeleteExamSchedule() {
                const response = await fetch(`http://127.0.0.1:8000/api/v1/exam_schedule/${this.form_delete}/delete`, {
                        method: 'DELETE',
                        headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        }
                    }
                );
                if (response.status !== 204) {
                    alert(JSON.stringify(await response.json(), null, 2));
                }

                this.isDeleteVisible = !this.isDeleteVisible
                await this.loadListExamSchedule()
            },

    goCreate() {
                this.isCreateVisible = !this.isCreateVisible
            },
            CreateExamSchedule() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/exam_schedule/create",
                    type: "POST",
                    data: {
                        exam_id: this.form_create.exam_id,
                        complition_date_exam: this.form_create.complition_date_exam,
                        the_audience: this.form_create.the_audience,
                        group_number: this.form_create.group_number,
                    },
                    success: (response) => {
                        this.isCreateVisible = !this.isCreateVisible
                      this.loadListExamSchedule()
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Введены некорректные данные")
                        }
                    }
                })
            },
  }
}
</script>

<style scoped>
.button-wrapper{
  padding: 30px;
}

</style>