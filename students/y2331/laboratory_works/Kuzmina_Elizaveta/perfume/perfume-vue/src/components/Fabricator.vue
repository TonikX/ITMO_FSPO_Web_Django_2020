<template>
  <div style="width: 100%">
    <mu-row v-for="item in items" :key="item.id">
      <mu-expansion-panel style="width: 100%;text-align: left;">
        <div slot="header">{{item.name_fabricator}}</div>
        <p>Страна: {{item.country}}</p>
        <p>Юридический адрес: {{item.legal_address}}</p>
      </mu-expansion-panel>
    </mu-row>
  </div>
</template>

<script>
  export default {
    name: "Fabricator",
    props: {
      items: ''
    },
    created() {
      this.$emit('giveName', 'Просмотр производителей');
    },
  }
</script>

<style scoped>

</style>
