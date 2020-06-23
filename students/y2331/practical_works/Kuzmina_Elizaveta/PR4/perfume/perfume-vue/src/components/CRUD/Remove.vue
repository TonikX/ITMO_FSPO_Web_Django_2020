<template>
  <div>
    <mu-button icon color="deepPurple800" @click="signalDelete" delete v-if="remove">
      <mu-icon value="delete"></mu-icon>
    </mu-button>
  </div>
</template>

<script>
  export default {
    name: "Remove",
    props: {
      model: '',
      id: ''
    },
    data() {
      return {
        remove: true
      }
    },
    methods: {
      signalDelete() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/perfume/" + this.$route.params.model + '/' + this.id,
          type: "DELETE",
          data: {},
          success: (response) => {
            this.remove = false;
            this.$emit('itemDelete',);
          },
          error: (response) => {
            alert("Не удалось произвести удаление. Повторите попытку позже.")
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
