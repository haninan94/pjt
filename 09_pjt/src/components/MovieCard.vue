<template>
  <div class="col">
    <div class="card h-100" style="max-width: 400px;">
      <img :src="img_url" alt="">
      <div class="card-body">
        <div class="card-title">
          <p>영화 제목 : {{ movie.title }}</p>
        </div>
        <div class="card-body">
          <p>줄거리 : {{ movie.overview }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  data() {
    return {
      img_url: 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
    }
  }
}
</script>

<style>

</style>