<template>
  <div>
    <div class="row row-cols-1 row-cols-md-3 g-4 custom">
      <MovieCard
      v-for="movie in movies"
      :key="movie.id"
      :movie=movie
      />
    </div>
  </div>

  
</template>

<script>
import MovieCard from '@/components/MovieCard'
import axios from 'axios'

export default {
  name: 'MovieView',
  data() {
    return {
      movies: null,
    }
  },
  components: {
    MovieCard
  },
  methods: {
    createMovies() {
      axios.get(this.$store.state.movies_url)
        .then((response) => {
          this.movies = response.data.results
        })
        .catch((error) => {
          console.log(error)

        })
      console.log(this.movies)
    }
  },
  created() {
    this.createMovies()
  }
  
}
</script>

<style>
  .custom {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>