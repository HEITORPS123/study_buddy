<template>
  <v-container>
    <v-card
      rounded="xl"
      color="#FFFFFF"
      elevation="10"
      max-width="800px"
      height="600px"
      class="bigrect-group-posts"
    >

      <v-row>
        <h1 class="pa-8"> Posts </h1>
        <v-spacer></v-spacer>
      </v-row>

      <v-row>
        <v-sheet
          class="ma-5"
          outlined
          rounded
        >
          <v-responsive
            class="overflow-y-auto"
            max-height="380px"
          >
            <v-row
              v-for="(post) in posts" :key="posts.findIndex(x=>x==post)"
            >
              <v-card
                class="pa-6"
                height="auto"
                width="800px"
              >
                <v-row>
                  <v-col cols="2">
                    <v-img :src="user_avatar"
                    height="90px"
                    width="90px"
                    class="ma-4"
                    ></v-img>
                  </v-col>
                  <v-col>
                    <v-row>
                      <p class="date-post"> {{ post.username }} </p>
                    </v-row>
                    <v-row>
                      <p class="content-post"> {{ post.content }} </p>
                    </v-row>
                  </v-col>
                </v-row>
              </v-card>
            </v-row>
          </v-responsive>
        </v-sheet>
      </v-row>

      <v-row>
        <v-spacer></v-spacer>
        <v-dialog
          transition="dialog-bottom-transition"
          width="auto"
          height="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn 
              class="ma-3"
              color="blue"
              v-bind="attrs"
              v-on="on"
            >
              <h3> Criar Post </h3>
            </v-btn>
          </template>
          <template v-slot:default="dialog">
            <v-card
              width="570px"
              height="400px"
            >
              <v-row>
                <v-col>
                  <h2 class="ma-5"> Criar Post </h2>
                </v-col>
                <v-col>
                  <v-card-actions class="justify-end">
                    <v-btn
                      class="ma-3"
                      color="blue"
                      @click="dialog.value = false"
                    >Fechar</v-btn>
                  </v-card-actions>
                </v-col>
              </v-row>

              <v-row>
                <v-textarea
                clearable
                label="Escreva aqui"
                v-model="postcontent"
                height="120px"
                class="ma-8"
                ></v-textarea>
              </v-row>
              <v-row>
                <v-spacer/>
                <v-btn
                  class="ma-1"
                  color="blue"
                  @click="post();dialog.value=false"
                >
                  <h3> Postar </h3>
                </v-btn>
                <v-spacer/>
              </v-row>
            </v-card>
          </template>
        </v-dialog>
        <v-spacer></v-spacer>
      </v-row>

    </v-card>
  </v-container>
</template>
<script>
import axios from 'axios';
export default {
  data: () => ({
    user_avatar: "https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png",
    posts: []
  }),
  async mounted () {
      let url = 'http://localhost:8890/getPosts'
      let data = {
          id: parseInt(this.$route.params.group_id),
      }

      const response = await axios.post(url,data)
      this.posts = response.data
  },
  methods: {
    async post () {
      let user_id = document.cookie.split('=')[1]

      let url = 'http://localhost:8890/createPost'
      let data = {
          group_id: parseInt(this.$route.params.group_id),
          user_id: parseInt(user_id),
          content: this.postcontent
      }

      await axios.post(url,data)

      this.postcontent=""

      let url2 = 'http://localhost:8890/getPosts'
      let data2 = {
          id: parseInt(this.$route.params.group_id),
      }

      const response2 = await axios.post(url2,data2)
      this.posts = response2.data
    }
  }
}
</script>
<style>
.bigrect-group-posts {
  margin-top: 30px;
  margin-bottom: 20px;
  margin-left: 170px;
}
.date-post {
  margin-top: 4px;
  margin-bottom: 4px;
  margin-left: 4px;
  margin-right: 4px;
}
.content-post {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 4px;
  padding-right: 4px;
}
</style>
