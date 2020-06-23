<template>
  <div style="width: 100%">
    <mu-row v-for="item in items" v-bind:key="item.id">
      <mu-expansion-panel style="width: 100%;text-align: left;">
        <div slot="header">{{item.name_firm}}</div>
        Страна: {{item.country}}
        <p>Юридический адрес: {{item.legal_address}}</p>
        <p v-text="'Тип фирмы: '+typeFirm(item.type_firm)"></p>
      </mu-expansion-panel>
    </mu-row>
  </div>
</template>

<script>
  export default {
    name: "Firm",
    props: {
      items: ''
    },
    created() {
      this.$emit('giveName', 'Просмотр фирм');
    },
    methods: {
      typeFirm(firm) {
        return firm === 'S' ? 'Seller' : 'Buyer'
      },
    }
  }
</script>

<style scoped>

</style>
