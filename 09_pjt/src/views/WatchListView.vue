<template>
  <div>
    <WatchListForm/>
    <WatchListItem
    v-for="(item, index) in watchListItems"
    :key="index"
    :item="item"
    />
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm/'
import WatchListItem from '@/components/WatchListItem/'

export default {
  naem: 'WatchListView',
  components: {
    WatchListForm,
    WatchListItem,  
  },
  computed: {
    watchListItems() {
      return this.$store.state.watch_list
    }
  },
}
</script>

<style>

</style>