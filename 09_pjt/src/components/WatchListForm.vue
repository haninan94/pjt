<template>
  <div class="bg-color">
    <h1>보고싶은 영화</h1>
    <input type="text" v-model="watch_movie" @keyup.enter="createWatchList">
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      watch_movie: null,
    }
  },
  methods: {
    createWatchList() {
      this.$store.dispatch('createWatchList', this.watch_movie)
      this.watch_movie = null
    }
  }

}
</script>

<style>
.bg-color{
  background-color: #87cee8
}
</style>