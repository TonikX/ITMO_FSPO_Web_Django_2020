<template>
  <div style="width: 100%">
    <mu-row v-for="item in items" :key="item.id">
      <Remove v-bind:id="item.id" v-bind:model="'product'" @itemDelete="reload"></Remove>
      <EditProduct v-bind:item="item" @reload="reload"></EditProduct>
      <span style="width: 92%">
            <mu-expansion-panel style="width: 100%;text-align: left;">
                <div slot="header">{{item.name}}</div>
                <p v-text="'Тип: '+typePerfume(item.type)"></p>
                <p>Срок годности: {{item.shelf_life}} год(а)</p>
                <p v-text="'Пол: '+typeSex(item.sex)"></p>
                <mu-expansion-panel>
                    <div slot="header">Производитель</div>
                    Название производителя: {{item.fabricator.name_fabricator}}
                    <p>Страна: {{item.fabricator.country}}</p>
                    <p>Юридический адрес: {{item.fabricator.legal_address}}</p>
                </mu-expansion-panel>
            </mu-expansion-panel>
            </span>
    </mu-row>
  </div>
</template>

<script>
  import Remove from "./CRUD/Remove";
  import EditProduct from "./CRUD/EditProduct";

  export default {
    name: "Product",
    components: {
      EditProduct,
      Remove
    },
    props: {
      items: ''
    },
    created() {
      this.$emit('giveName', 'Редактирование товаров');
    },
    methods: {
      typePerfume(type) {
        switch (type) {
          case 'PA':
            return 'Parfum';
          case 'EP':
            return 'Eau de Parfum';
          case 'ET':
            return 'Eau de Toilette';
          case 'EC':
            return 'Eau de Cologne';
          case 'EF':
            return 'Eau Fraiche';
        }
      },
      typeSex(sex) {
        if (sex === 'F') return 'Female';
        else if (sex === 'M') return 'Male';
        else return 'Unisex'
      },
      reload() {
        this.$emit('getPanels',);
      },
    }
  }
</script>

<style scoped>

</style>
