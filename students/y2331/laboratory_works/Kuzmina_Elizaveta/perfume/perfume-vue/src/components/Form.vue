<template>
  <div>
    <mu-appbar style="width: 100%;text-align: center" color="deepPurple500">
      {{name}}
      <mu-button flat slot="left" @click="mainWindow">
        <mu-icon value="home"></mu-icon>
      </mu-button>
      <mu-button v-if="this.$route.params.model === 'product' || this.$route.params.model === 'deal'" flat
                 slot="right" @click="post">
        <mu-icon value="add"></mu-icon>
        запись
      </mu-button>
    </mu-appbar>
    <mu-alert color="deepPurple50" delete v-if="isOpen" @delete="closeAlert">
      <mu-icon left value="info"></mu-icon>
      <div v-bind:style="{color:'Indigo'}">Для более подробной информации выберите интересующий элемент и
        раскройте его.
      </div>
    </mu-alert>
    <mu-row>
      <Broker v-if="this.$route.params.model === 'broker'" v-bind:items="items"
              @giveName="giveName"></Broker>
      <Firm v-if="this.$route.params.model === 'firm'" v-bind:items="items"
            @giveName="giveName"></Firm>
      <Deal v-if="this.$route.params.model === 'deal'" v-bind:items="items"
            @giveName="giveName" @getPanels="getPanels"></Deal>
      <Product v-if="this.$route.params.model === 'product'" v-bind:items="items"
               @giveName="giveName" @getPanels="getPanels"></Product>
      <Fabricator v-if="this.$route.params.model === 'fabricator'" v-bind:items="items"
                  @giveName="giveName"></Fabricator>
    </mu-row>
    <mu-row v-if="this.$route.params.model === 'product'">
      <CreateProduct v-bind:openAlert="open" @reload="getPanels" @closePost="closePost"
                     ref="openProduct"></CreateProduct>
    </mu-row>
    <mu-row v-if="this.$route.params.model === 'deal'">
      <CreateDeal v-bind:openAlert="open" @reload="getPanels" @closePost="closePost" ref="openDeal"></CreateDeal>
    </mu-row>
  </div>
</template>

<script>
  import Broker from "@/components/Broker";
  import Firm from "@/components/Firm";
  import Deal from "@/components/Deal";
  import Product from "./Product";
  import Fabricator from "./Fabricator";
  import EditProduct from "./CRUD/EditProduct";
  import EditDeal from "./CRUD/EditDeal";
  import CreateDeal from "./CRUD/CreateDeal";
  import CreateProduct from "./CRUD/CreateProduct";

  export default {
    name: "Form",
    components: {
      CreateProduct,
      CreateDeal,
      EditDeal,
      EditProduct,
      Fabricator,
      Firm,
      Broker,
      Deal,
      Product,
    },
    props: {
      model: '',
    },
    data() {
      return {
        items: '',
        name: '',
        isOpen: true,
        open: false
      }
    },
    created() {
      $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')},
      });
      this.getPanels();
    },
    methods: {
      giveName(name) {
        this.name = name;
      },
      closeAlert() {
        this.isOpen = false
      },
      mainWindow() {
        this.$router.push({name: "home"})
      },
      getPanels() {
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/perfume/" + this.$route.params.model + '/',
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
      post() {
        if (this.$route.params.model === 'deal') this.$refs.openDeal.openAlertDialog();
        else this.$refs.openProduct.openAlertDialog();
        this.open = true;
      },
      closePost() {
        this.open = false;
      },
    }

  }
</script>

<style scoped>

</style>
