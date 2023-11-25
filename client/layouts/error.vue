<template>
  <v-app dark>
    <h1 v-if="error.statusCode === 404">
      {{ pageNotFound }}
    </h1>
    <h1 v-else>
      {{ otherError }}
    </h1>
    <NuxtLink to="/">
      Home page
    </NuxtLink>
    <!-- <v-overlay :value="step2 < 6" :class="`wel-overlay overlay-step-${properties[step2].class}`"></v-overlay>
  
  
  
  
      <v-dialog v-model="ins" width="250" persistent :content-class="`${properties[step2].class}-dialog`" hide-overlay>
        <v-card>
          <v-card-title>
            {{properties[step2].title}}
          </v-card-title>
          <v-card-text>
            {{properties[step2].desc}}
          </v-card-text>
          <v-card-actions>
            <v-btn v-if="step2==1" text @click="ins = false">Cancel</v-btn>
            <v-btn v-else-if="step2==5" @click="step2 = 6;ins=false">No, Got it</v-btn>
            <v-btn v-else text @click="step2 -= 1">Previous</v-btn>
            <v-spacer></v-spacer>
            <a v-if="step2==5" target="_blank" href="/usermanual.pdf"><v-btn color="primary">Download</v-btn></a>
            <v-btn v-else-if="step2==4" color="primary" text @click="step2+=1">OK</v-btn>
            <v-btn v-else color="primary" text @click="step2+=1" >Next</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog> -->
  </v-app>
</template>

<script>
export default {
  name: 'EmptyLayout',
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred',
      // properties: [
        //   {title: 'None', desc: 'This is Test', class: 'none'},
        //   {title: 'Navbar', desc: 'This is Navbar, where all the main links will be visible.', class: 'navbar'},
        //   {title: 'Notifications', desc: 'All your Notifications can be accessed through the icon right here', class: 'notifications'},
        //   {title: 'User Details', desc: 'The Icon is a Menu with several Profile related Options', class: 'profile'},
        //   {title: 'Search', desc: 'This is Searchbar, you can search whatever you want from here', class: 'search'},
        //   {title: 'Stuck Somewhere?', desc: 'You can download the User Manual for more precise description of the app.', class: 'stuck'},
        //   {title: 'Done', desc: 'Tour Completed.', class: 'done'},
        // ]
    }
  },
  head () {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>
