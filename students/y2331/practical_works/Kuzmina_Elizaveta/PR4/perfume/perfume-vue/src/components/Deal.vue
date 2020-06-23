<template>
  <div style="width: 100%">
    <mu-row v-for="item in items" :key="item.id">
      <Remove v-bind:id="item.id" v-bind:model="'deal'" @itemDelete="reload"></Remove>
      <EditDeal v-bind:item="item" @reload="reload"></EditDeal>
      <span style="width: 92%">
            <mu-expansion-panel style="width: 100%;text-align: left;">
                <div slot="header">{{item.date_deal}}</div>
                <mu-expansion-panel style="width: 100%;margin-top: 10px">
                    <div slot="header">Маклер</div>
                    Имя: {{item.broker.first_name}}
                    <p>Фамилия: {{item.broker.second_name}}</p>
                    <p>Адрес: {{item.broker.address}}</p>
                    <p>Дата рождения: {{item.broker.birthdate}}</p>
                    <mu-expansion-panel v-if="item.broker.broker" style="width: 100%;">
                        <div slot="header">Профиль</div>
                        Никнейм: {{item.broker.broker.username}}
                        <p>Почта: {{item.broker.broker.email}}</p>
                    </mu-expansion-panel>
                </mu-expansion-panel>
                <mu-expansion-panel
                  v-for="firms in massive={buyer: {info: item.buyer, name: 'Покупатель'}, seller: {info: item.seller, name: 'Продавец'}}"
                  :key="firms.info.id + ' firm'">
                    <div slot="header">{{firms.name}}</div>
                    Название фирмы: {{firms.info.name_firm}}
                    <p>Страна: {{firms.info.country}}</p>
                    <p>Юридический адрес: {{firms.info.legal_address}}</p>
                    <p v-text="'Тип фирмы: '+typeFirm(firms.info.type_firm)"></p>
                </mu-expansion-panel>
                <Order v-bind:dealId="item.id"></Order>
            </mu-expansion-panel>
                </span>
    </mu-row>
  </div>
</template>

<script>
  import Order from "./Order";
  import Remove from "./CRUD/Remove";
  import EditDeal from "./CRUD/EditDeal";

  export default {
    name: "Deal",
    components: {EditDeal, Remove, Order},
    props: {
      items: '',
    },
    created() {
      this.$emit('giveName', 'Редактирование сделок');
    },
    methods: {
      typeFirm(firm) {
        return firm === 'S' ? 'Seller' : 'Buyer'
      },
      reload() {
        this.$emit('getPanels',);
      }
    }
  }
</script>

<style scoped>

</style>
