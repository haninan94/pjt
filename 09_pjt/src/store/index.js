// import axios from 'axios'
// import _ from 'lodash'
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies_url: 'https://api.themoviedb.org/3/movie/top_rated?api_key=a69f4da1b285b37e02bb3fb12539afd3&language=en-US&page=1',
    random_movie: null,
    watch_list: []
  },
  getters: {
  },
  mutations: {
    CREATE_WATCH_LIST(state, watchItem) {
      state.watch_list.push(watchItem)
    },
    UPDATE_ITEM_STATUS(state, Item) {
      state.watch_list = state.watch_list.filter((item) => {
        if (item === Item) {
          item.isCompleted = !item.isCompleted
        }
        return item
      })
    }
    
  },
  actions: {
    createWatchList(context, watch_list) {
      const watchItem = {
        title: watch_list,
        isCompleted: false,
      }
      context.commit('CREATE_WATCH_LIST', watchItem)
    },
    updateItemStatus(context, Item) {
      context.commit('UPDATE_ITEM_STATUS', Item)
    }
  },
  modules: {
  },
  // created() {
  //   this.GET_RANDOM_MOVIE()
  // }
})
