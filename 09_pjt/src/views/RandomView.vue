<template>
  <div>
    <br>
    <div>
      <button @click="getRandomMovie" class="button pick">Pick</button>
      <br>
      <br>
      <img :src="movie_poster_path" alt="">
    </div>
      <p>영화 제목 : {{ movie?.title }}</p>
      <p>영화 줄거리 : {{ movie?.overview }}</p>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'RandomView',
  data() {
    return {
      movie: this.$store.state.random_movie,
      movie_poster_path: null,
    }
  },
  methods: {
    getRandomMovie() {
      // this.$store.commit('GET_RANDOM_MOVIE')
      // this.movie = this.$store.state.random_movie
      axios.get(this.$store.state.movies_url)
        .then((response) => {
          const movies = response.data.results
          this.movie =  _.sample(movies)
          this.movie_poster_path = 'https://image.tmdb.org/t/p/w300/' + this.movie.poster_path
        })
    }
  },
  created() {
    this.getRandomMovie()
  },

}
</script>

<style>
.button:hover {
  background-color: #90ee99;
  transition: 0.7s;
  border-color: white;
}
.pick{
  border-color: white;
  border-radius: 12px;
  width: 300px;
}
</style>