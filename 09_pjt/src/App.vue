<template>
  <div id="app" class="container">
    <header>
      <img src="./assets/logo3.png" alt="">
      <nav>
        <router-link :to="{ name: 'movies' }" class="logo">Movies</router-link>|
        <router-link :to="{ name: 'random' }">Random</router-link> |
        <router-link :to="{ name: 'watchlist' }">Watch List</router-link>
      </nav>
    </header>
    <router-view/>
  </div>
</template>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: white;
}

.logo{
  text-decoration: none;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #00ced0
}
</style>