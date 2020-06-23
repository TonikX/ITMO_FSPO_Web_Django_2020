<template>
  <mu-paper style="width: 100%;margin-top: 40px" :z-depth="5">
    <mu-list textline="two-line">
      <mu-list-item v-for="map in choices" :key="map[0]" button :ripple="false" @click="openItem(map[3])">
        <mu-list-item-action>
          <mu-icon v-model="map[2]" color="deepPurple500"></mu-icon>
        </mu-list-item-action>
        <mu-list-item-content>
          <mu-list-item-title>{{map[0]}}</mu-list-item-title>
          <mu-list-item-sub-title>{{map[1]}}</mu-list-item-sub-title>
        </mu-list-item-content>
      </mu-list-item>
    </mu-list>
  </mu-paper>
</template>

<script>
  export default {
    name: "Menu",
    data() {
      return {
        choices: '',
      }
    },
    created() {
      this.loadMenu()
    },
    methods: {
      loadMenu() {
        this.choices = [
          ['Маклеры', 'Просмотр маклеров', 'assignment_ind', 'broker'],
          ['Фирмы', 'Просмотр фирм', 'work', 'firm'],
          ['Сделки', 'Редактирование сделок', 'local_atm', 'deal'],
          ['Товары', 'Редактирование товаров', 'whatshot', 'product'],
          ['Производители', 'Просмотр производителей', 'group', 'fabricator'],
        ];
      },
      openItem(model) {
        this.$router.push({name: 'form', params: {model: model}})
      }
    }
  }
</script>

<style scoped>

</style>
