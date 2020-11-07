<template>
<mu-container>
  <mu-appbar style="width: 100%;" color="#d7ccc8" title="Журнал сессии"></mu-appbar>
  <img vspace="20" src="https://sun9-58.userapi.com/w1jncFH6fgLHBCkGJcvlmyK9C39SBcMX9Q_ytA/-jSXMPk2Emk.jpg" width="350" height="300">
  <br>
  <br>
  <mu-flex justify-content="center" align-items="center" class="button-wrapper" >
    <mu-button @click="goExamSchedule" round color="#a1887f">Расписание экзаменов</mu-button>
    <mu-button @click="goStudent" round color="#a1887f">Список студентов</mu-button>
    <mu-button @click="goTeacher" round color="#a1887f">Список преподавателей</mu-button>
    <mu-button @click="goDiscipline" round color="#a1887f">Список дисциплин</mu-button>
    <mu-button @click="goExam" round color="#a1887f">Результаты экзаменов</mu-button>
  </mu-flex>
  <br/>
  <br/>
</mu-container>
</template>

<script>
  export default {
    name: "Home",
    methods: {
            goExamSchedule() {
                this.$router.push({name: "schedule"})
            },
            goStudent() {
                this.$router.push({name: "student"})
            },
            goDiscipline() {
                this.$router.push({name: "discipline"})
            },
            goTeacher() {
                this.$router.push({name: "teacher"})
            },
            goExam() {
                this.$router.push({name: "exam"})
            },
    },
  }
</script>


<style lang="less">

.button-wrapper {
  text-align: center;
  height: 5px;
  position: marker;
  justify-content: flex-end;

  .mu-button{
    margin: 20px;
    vertical-align: middle;

  }
  a.mu-button {
    text-decoration: none;
  }
}

</style>