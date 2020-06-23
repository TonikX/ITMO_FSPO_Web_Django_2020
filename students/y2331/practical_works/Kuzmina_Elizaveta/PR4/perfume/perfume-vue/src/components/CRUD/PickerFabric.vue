<template>
  <div>
    <mu-dialog width="360" transition="slide-bottom" fullscreen :open.sync="openFullscreen">
      <mu-appbar color="deepPurple500" title="Производители">
        <mu-button slot="left" icon @click="closeFullscreenDialog">
          <mu-icon value="close"></mu-icon>
        </mu-button>
      </mu-appbar>
      <mu-row v-for="fabric in items" :key="fabric.id">
        <mu-expansion-panel style="width: 100%;text-align: left;">
          <div slot="header">{{fabric.name_fabricator}}</div>
          <p>Страна: {{fabric.country}}</p>
          <p>Юридический адрес: {{fabric.legal_address}}</p>
          <mu-button color="deepPurple500"
                     @click="closeFullscreenDialog(fabric.id,fabric.name_fabricator)">Выбрать
          </mu-button>
        </mu-expansion-panel>
      </mu-row>
    </mu-dialog>
  </div>
</template>

<script>
  export default {
    name: "PickerFabric",
    props: {
      items: '',
      openFullscreen: false
    },
    methods: {
      closeFullscreenDialog(id, name) {
        this.$emit('closeFullscreenDialog', false, id, name);
      }
    }
  }
</script>

<style scoped>

</style>
