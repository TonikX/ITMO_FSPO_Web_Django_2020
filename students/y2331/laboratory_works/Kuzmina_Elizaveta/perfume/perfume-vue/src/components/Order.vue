<template>
  <div style="width: 100%">
    <mu-button color="deepPurple500" style="margin-top: 10px" @click="openFullscreenDialog">
      <mu-icon value="add"></mu-icon>
      Открыть заказы
    </mu-button>
    <mu-dialog width="360" transition="slide-bottom" fullscreen :open.sync="openFullscreen">
      <mu-appbar color="deepPurple500" title="Заказы">
        <mu-button slot="left" icon @click="closeFullscreenDialog">
          <mu-icon value="close"></mu-icon>
        </mu-button>
      </mu-appbar>
      <mu-expansion-panel v-if="dealItem" v-for="item in dealItem" :key="dealItem.id">
        <div slot="header">{{item.product.name}}</div>
        Количество: {{item.number_sold}}
        <p>Цена продавца: {{item.cost_seller}} руб.</p>
        <p>Цена маклера: {{item.cost_broker}} руб.</p>
        <mu-expansion-panel>
          <div slot="header">Информация о продукте</div>
          <p v-text="'Тип: '+typePerfume(item.product.type)"></p>
          <p>Срок годности: {{item.product.shelf_life}} год(а)</p>
          <p v-text="'Пол: '+typeSex(item.product.sex)"></p>
        </mu-expansion-panel>
      </mu-expansion-panel>
      <mu-alert color="deepPurpleA100" v-if="dealItem.length === 0" style="margin-top: 20px;">
        <mu-icon left value="info"></mu-icon>
        Пока что заказов для данной сделки нет.
      </mu-alert>
    </mu-dialog>
  </div>
</template>

<script>
  export default {
    name: "Order",
    props: {
      dealId: '',
    },
    data() {
      return {
        openFullscreen: false,
        dealItem: ''
      };
    },
    methods: {
      openFullscreenDialog() {
        this.openFullscreen = true;
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/perfume/order_deal/",
          type: "GET",
          data: {
            "deal": this.dealId
          },
          success: (response) => {
            this.dealItem = response.data.data;
          },
          error: (response) => {
            alert("Произошла ошибка. Повторите попытку позже...");
            this.openFullscreen = false;
          }
        });
      },
      closeFullscreenDialog() {
        this.openFullscreen = false;
      },
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
      }
    },
  }
</script>

<style scoped>

</style>
