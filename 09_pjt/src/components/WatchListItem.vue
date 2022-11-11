<template>
  <div @click="updateItemStatus" 
  :class="{ 'is-completed': item.isCompleted, 'is-uncompleted': !item.isCompleted}">
    {{ item.title }}
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    item: Object,
  },
  methods: {
    updateItemStatus() {
      this.$store.dispatch('updateItemStatus', this.item)
    }
  },
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
    background-color: grey;
  }
  .is-uncompleted {
    background-color: lightgrey;
  }
</style>