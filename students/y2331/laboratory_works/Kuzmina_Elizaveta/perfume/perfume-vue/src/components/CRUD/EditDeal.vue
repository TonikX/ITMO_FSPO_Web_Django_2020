<template>
  <div>
    <mu-button icon color="deepPurple800" @click="openAlertDialog">
      <mu-icon value="edit"></mu-icon>
    </mu-button>
    <mu-dialog title="Редактор сделки" width="400" max-width="80%" :esc-press-close="false"
               :overlay-close="false" :open.sync="openAlert">
      <mu-form :model="form" :label-position="labelPosition">
        <mu-date-input icon="today" v-model="form.date" label-float full-width value-format="YYYY-MM-DD"
                       :date-time-format="enDateFormat" color="deepPurple800" display-color="deepPurple800">
        </mu-date-input>
        <mu-form-item>
          <mu-button color="deepPurple800" @click="seller">
            <mu-icon value="add"></mu-icon>
            Продавец
          </mu-button>
          <mu-button color="deepPurple800" @click="buyer">
            <mu-icon value="add"></mu-icon>
            Покупатель
          </mu-button>
          <Picker v-bind:openFullscreen="openFullscreen" v-bind:items="firm"
                  @closeFullscreenDialog="closeFullscreenDialog"></Picker>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-text="'Продавец: '+names.sellerName"></mu-text-field>
          <mu-text-field v-text="'Покупатель '+names.buyerName"></mu-text-field>
        </mu-form-item>
      </mu-form>
      <mu-button slot="actions" flat color="deepPurple800" @click="closeAlertDialog">Отменить</mu-button>
      <mu-button slot="actions" flat color="deepPurple800" @click="closeSaveAlertDialog">Изменить</mu-button>
    </mu-dialog>
  </div>
</template>

<script>
  const dayAbbreviation = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
  const dayList = ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'];
  const monthList = ['Янв', 'Февр', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент',
    'Окт', 'Нояб', 'Дек'];
  const monthLongList = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];

  const enDateFormat = {
    formatDisplay(date) {
      return `${dayList[date.getDay()]}, ${monthList[date.getMonth()]} ${date.getDate()}`;
    },
    formatMonth(date) {
      return `${monthLongList[date.getMonth()]} ${date.getFullYear()}`;
    },
    getWeekDayArray(firstDayOfWeek) {
      let beforeArray = [];
      let afterArray = [];
      for (let i = 0; i < dayAbbreviation.length; i++) {
        if (i < firstDayOfWeek) {
          afterArray.push(dayAbbreviation[i]);
        } else {
          beforeArray.push(dayAbbreviation[i]);
        }
      }
      return beforeArray.concat(afterArray);
    },
    getMonthList() {
      return monthList;
    }
  };
  import Picker from "./Picker";

  export default {
    name: "EditDeal",
    components: {
      Picker
    },
    props: {
      item: '',
    },
    data() {
      return {
        openAlert: false,
        labelPosition: 'left',
        form: {
          date: this.item.date_deal,
          sellerId: this.item.seller.id,
          buyerId: this.item.buyer.id,
        },
        names: {
          sellerName: this.item.seller.name_firm,
          buyerName: this.item.buyer.name_firm,
        },
        items: '',
        firm: [],
        openFullscreen: false,
        enDateFormat
      };
    },
    methods: {
      openAlertDialog() {
        this.openAlert = true;
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/perfume/firm/",
          type: "GET",
          data: {},
          success: (response) => {
            this.items = response.data.data
            // console.log(response)
          },
          error: (response) => {
            alert("Проблемы с подключением к серверу. Повторите попытку позже.")
          }
        })
      },
      closeAlertDialog() {
        this.form.date = this.item.date_deal;
        this.form.sellerId = this.item.seller.id;
        this.form.buyerId = this.item.buyer.id;
        this.openAlert = false;
      },
      closeSaveAlertDialog() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/perfume/deal/" + this.item.id,
          type: "PUT",
          data: {
            date_deal: this.form.date,
            seller: this.form.sellerId,
            buyer: this.form.buyerId
          },
          success: (response) => {
            // console.log(response);
            this.$emit('reload',);
            this.openAlert = false;
          },
          error: (response) => {
            alert("Проблемы с изменением элемента. Повторите попытку позже.");
            this.openAlert = false;
          }
        })
      },
      seller() {
        var items2 = [];
        for (var element of this.items) {
          if (element['type_firm'] === 'S')
            items2.splice(0, 0, element)
        }
        this.firm = items2;
        this.openFullscreen = true;
        // console.log(this.firm)
      },
      buyer() {
        var items2 = [];
        for (var element of this.items) {
          if (element['type_firm'] === 'B')
            items2.splice(0, 0, element)
        }
        this.firm = items2;
        this.openFullscreen = true;
        // console.log(this.firm)
      },
      closeFullscreenDialog(openFullscreen, id, type, name) {
        this.openFullscreen = openFullscreen;
        if (name !== undefined) {
          if (type === 'S') {
            this.form.sellerId = id;
            this.names.sellerName = name
          } else {
            this.form.buyerId = id;
            this.names.buyerName = name
          }
        }
      }
    },
  }
</script>

<style scoped>

</style>
