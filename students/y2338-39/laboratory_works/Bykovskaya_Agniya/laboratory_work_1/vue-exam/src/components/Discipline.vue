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
                            <mu-list-item-title>Дисциплины</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button href="#/exam">
                            <mu-list-item-title>Результаты экзаменов</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
         Список дисциплин

  <mu-button flat slot="right" href="#/">На главную</mu-button>
       </mu-appbar>
 <mu-row>
            <mu-col align="center">
                <table>
                  <thead>
                  <tr>
                    <th>Код дисцилины</th>
                    <th>Название дисциплины</th>
                    </tr>
                  </thead>
                  <tbody>
                        <tr v-for="discipline in listDiscipline" :key="discipline.id">
                        <td>{{discipline.discipline_code}}</td>
                        <td>{{discipline.discipline_name}}</td>
                        </tr>
                  </tbody>
                </table>
                 <img vspace="60" src="https://sun9-55.userapi.com/rMMm8OW5M_2dHWSJllRlis7qvDr-yd78bkM61g/n0El-kd0Uzg.jpg" width="200" height="100">
            </mu-col>
        </mu-row>

    </mu-container>
</template>

<script>
export default {
  name: "Discipline",
  components: {},
  data() {
    return {
      listDiscipline: [],
    }
  },
  created(){
    this.loadListDiscipline()
  },
  methods: {
    async loadListDiscipline() {
      this.listDiscipline = await fetch(
          `http://127.0.0.1:8000/api/v1/discipline/`
      ).then(response => response.json())
    },
  }
}
</script>

<style scoped>

</style>