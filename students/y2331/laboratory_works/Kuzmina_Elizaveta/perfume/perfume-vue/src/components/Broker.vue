<template>
  <div style="width: 100%">
    <mu-row v-for="item in items" :key="item.id">
      <mu-expansion-panel style="width: 100%;text-align: left;">
        <div slot="header">{{item.first_name}} {{item.second_name}}</div>
        Адрес: {{item.address}}
        <p>Дата рождения: {{item.birthdate}}</p>
        <mu-expansion-panel v-if="item.broker" style="width: 100%;">
          <div slot="header">Профиль</div>
          Никнейм: {{item.broker.username}}
          <p>Почта: {{item.broker.email}}</p>
        </mu-expansion-panel>
      </mu-expansion-panel>
    </mu-row>
  </div>
</template>

<script>
  export default {
    name: "Broker",
    props: {
      items: ''
    },
    created() {
      this.$emit('giveName', 'Просмотр маклеров');
    }
  }
</script>

<style scoped>

</style>
