<template>
  <div>
    <mu-button icon color="deepPurple800" @click="openAlertDialog">
      <mu-icon value="edit"></mu-icon>
    </mu-button>
    <mu-dialog title="Редактор товара" width="400" max-width="80%" :esc-press-close="false"
               :overlay-close="false" :open.sync="openAlert">
      <mu-form :model="form" :label-position="labelPosition" ref="form">
        <mu-form-item prop="name" label="Название товара" :rules="lineRule">
          <mu-text-field v-model="form.name" color="deepPurple800"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="select" label="Тип">
          <mu-select v-model="form.type">
            <mu-option v-for="(option,index) in options" :key="index" :label="option"
                       :value="option"></mu-option>
          </mu-select>
        </mu-form-item>
        <mu-form-item prop="shelf_life" label="Срок годности" :rules="numberRule">
          <mu-text-field v-model.number="form.shelf_life" color="deepPurple800" type="number" min="1"
                         max="30"></mu-text-field>
        </mu-form-item>
        <mu-form-item prop="select" label="Пол">
          <mu-select v-model="form.sex">
            <mu-option v-for="(option,index) in sex" :key="index" :label="option"
                       :value="option"></mu-option>
          </mu-select>
        </mu-form-item>
        <mu-form-item>
          <mu-button color="deepPurple800" @click="fabric">
            <mu-icon value="add"></mu-icon>
            Производитель
          </mu-button>
          <PickerFabric v-bind:openFullscreen="openFullscreen" v-bind:items="items"
                        @closeFullscreenDialog="closeFullscreenDialog"></PickerFabric>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-text="'Производитель: '+nameFabric"></mu-text-field>
        </mu-form-item>
      </mu-form>
      <mu-button slot="actions" flat color="deepPurple800" @click="closeAlertDialog">Отменить</mu-button>
      <mu-button slot="actions" flat color="deepPurple800" @click="closeSaveAlertDialog">Изменить</mu-button>
    </mu-dialog>
  </div>
</template>

<script>
  import PickerFabric from "./PickerFabric";

  export default {
    name: "EditProduct",
    components: {PickerFabric},
    props: {
      item: '',
    },
    data() {
      return {
        options: [
          'Parfum', 'Eau de Parfum', 'Eau de Toilette', 'Eau de Cologne',
          'Eau Fraiche',
        ],
        sex: ['Male', 'Female', 'Unisex'],
        openAlert: false,
        labelPosition: 'left',
        form: {
          name: this.item.name,
          type: this.typePerfume(this.item.type),
          shelf_life: this.item.shelf_life,
          sex: this.typeSex(this.item.sex),
          fabricatorId: this.item.fabricator.id,
        },
        nameFabric: this.item.fabricator.name_fabricator,
        items: '',
        openFullscreen: false,
        lineRule: [
          {validate: (val) => !!val, message: 'Поле должно быть заполнено'},
        ],
        numberRule: [
          {validate: (val) => !!val, message: 'Поле должно быть заполнено'},
          {validate: (val) => Number.isInteger(val), message: 'Поле должно быть целочисленным'},
        ],
        littleToBig: [['PA', 'EP', 'ET', 'EC', 'EF'],
          ['Parfum', 'Eau de Parfum', 'Eau de Toilette', 'Eau de Cologne', 'Eau Fraiche']
        ]
      }
    },
    methods: {
      openAlertDialog() {
        this.openAlert = true;
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/perfume/fabricator/",
          type: "GET",
          data: {},
          success: (response) => {
            this.items = response.data.data;
            // console.log(response)
          },
          error: (response) => {
            alert("Проблемы с подключением к серверу. Повторите попытку позже.")
          }
        })
      },
      closeAlertDialog() {
        this.form.name = this.item.name;
        this.form.type = this.typePerfume(this.item.type);
        this.form.shelf_life = this.item.shelf_life;
        this.form.sex = this.typeSex(this.item.sex);
        this.form.fabricatorId = this.item.fabricator.id;
        this.openAlert = false;
      },
      closeSaveAlertDialog() {
        this.$refs.form.validate().then((result) => {
          if (result === false) {
            alert('Какие-то поля заполнены неверно.');
          } else {
            $.ajax({
              url: "http://127.0.0.1:8000/api/v1/perfume/product/" + this.item.id,
              type: "PUT",
              data: {
                name: this.form.name,
                type: this.typeRevertPerfume(this.form.type),
                shelf_life: this.form.shelf_life,
                sex: this.typeRevertSex(this.form.sex),
                fabricator: this.form.fabricatorId,
              },
              success: (response) => {
                this.$emit('reload',);
                this.openAlert = false;
              },
              error: (response) => {
                alert("Проблемы с изменением элемента. Повторите попытку позже.");
                this.openAlert = false;
              }
            })
          }
        });

      },
      fabric() {
        this.openFullscreen = true;
      },
      closeFullscreenDialog(openFullscreen, id, name) {
        this.openFullscreen = openFullscreen;
        if (name !== undefined) {
          this.form.fabricatorId = id;
          this.nameFabric = name;
        }
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
      },
      typeRevertPerfume(type) {
        switch (type) {
          case 'Parfum':
            return 'PA';
          case 'Eau de Parfum':
            return 'EP';
          case 'Eau de Toilette':
            return 'ET';
          case 'Eau de Cologne':
            return 'EC';
          case 'Eau Fraiche':
            return 'EF';
        }
      },
      typeRevertSex(sex) {
        if (sex === 'Female') return 'F';
        else if (sex === 'Male') return 'M';
        else return 'U'
      },
    }
  }
</script>

<style scoped>

</style>
