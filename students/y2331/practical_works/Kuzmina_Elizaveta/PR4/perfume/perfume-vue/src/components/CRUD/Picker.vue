<template>
  <div>
    <mu-dialog width="360" transition="slide-bottom" fullscreen :open.sync="openFullscreen">
      <mu-appbar color="deepPurple500" title="Фирмы">
        <mu-button slot="left" icon @click="closeFullscreenDialog">
          <mu-icon value="close"></mu-icon>
        </mu-button>
      </mu-appbar>
      <mu-row v-for="firm in this.items" :key="firm.id">
        <mu-expansion-panel style="width: 100%;text-align: left;">
          <div slot="header">{{firm.name_firm}}</div>
          Страна: {{firm.country}}
          <p>Юридический адрес: {{firm.legal_address}}</p>
          <mu-button color="deepPurple500"
                     @click="closeFullscreenDialog(firm.id,firm.type_firm,firm.name_firm)">Выбрать
          </mu-button>
        </mu-expansion-panel>
      </mu-row>
    </mu-dialog>
  </div>
</template>

<script>
  export default {
    name: "Picker",
    props: {
      items: '',
      openFullscreen: false
    },
    methods: {
      closeFullscreenDialog(id, type, name) {
        this.$emit('closeFullscreenDialog', false, id, type, name);
      }
    }
  }
</script>

<style scoped>

</style>
