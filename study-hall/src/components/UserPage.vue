<template>
  <v-container>
    <v-card
      color="#FFFFFF"
      elevation=2
      height="900px"
      width="2100px"
      rounded="xl"
      class="bigrect-user"
    >
    <v-row>
        <v-col cols="4.5" class="usertext">
            <v-row>
                <v-img
                height="300"
                width="300"
                class="rounded-circle"
                src="../assets/image.jpeg"
                ></v-img>
              </v-row>

              <v-row class="subheadertext">
                <v-btn
                  depressed
                  elevation="0"
                  large
                  plain
                  width="350px"
                  @click="go_to_path('/edit')"
                >
                  <h1>Editar Perfil</h1>
                </v-btn>
              </v-row>

              <v-row class="subheadertext">
                <h1>Interests</h1>
              </v-row>

              <v-row>
              <v-item-group multiple>
                <v-item
                  v-for="n in (interesses.length - 1)"
                  :key="n"
                  v-slot="{ active, toggle }"
                >
                  <v-row class="tag">
                    <v-chip
                      active-class="purple--text"
                      :input-value="active"
                      @click="toggle"
                    >
                      {{ interesses[n] }}
                    </v-chip>
                  </v-row>
                </v-item>
              </v-item-group>
              </v-row>
          </v-col>

          <v-col>
            <v-divider vertical></v-divider>
          </v-col>

          <v-col cols="6.5" class="middletext">
              <v-container>
              <v-row>
                      <h1>{{ nome_completo }}</h1>
              </v-row>
              <v-row>
                      <h2>{{ idade }}</h2>
              </v-row>
              <v-row class="bigrect-user">
                <v-card
                  color="#D9D9D9"
                  elevation=2
                  height="650px"
                  width="500px"
                  rounded="xl"
                > 
                <v-row class="bigrecttitle">
                  <h2>About Me</h2>
                </v-row>
                <v-row class="usertext">
                  {{ about }}
                </v-row>
                </v-card>
                </v-row>
              </v-container>
          </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
  import axios from 'axios';
  
  export default {
    data: () => ({
      groups: ['Foo', 'Bar', 'Fizz', 'Buzz'],
      nome_completo: "exemplo",
      idade: 18,
      about: "",
      user_infos: {},
      interesses: []
    }),
    async mounted() {
      const url = 'http://localhost:8890/getUser'
      const user_id = parseInt(this.$route.params.user_id)

      const data = {
        id: user_id
      };

      const response = await axios.post(url,data, {headers:{'Access-Control-Request-Method': 'POST'}}).then(response => response.data)
      this.user_infos = response
      this.nome_completo = this.user_infos.fullname
      this.about = this.user_infos.about
      this.interesses = this.user_infos.interests.split('-')

      const data_nascimento = new Date(this.user_infos.birthday)
      const month_diff = Date.now() - data_nascimento.getTime()
      this.idade = Math.abs(new Date(month_diff).getUTCFullYear() - 1970)
    },
    methods: {
      go_to_path (path) {
        if (this.$route.path !== path) {
          this.$router.push(path);
        }
      }
    }
  }
</script>

<style>
.usertext {
  border-right: 40px solid transparent;
  border-left: 40px solid transparent;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

.bigrecttitle {
  border-left: 200px solid transparent;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

.middletext {
  border-right: 70px solid transparent;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

.subheadertext {
  border-top: 30px solid transparent;
  border-bottom: 30px solid transparent;
}

.buttonregister {
  background-color: #0D1A8F;
  color: white;
}

    .bigrect-user {
  border-top: 30px solid transparent;
  border-bottom: 30px solid transparent;
}

.uploading-image{
    display:flex;
  }
  
.tag {
  border-top: 15px solid transparent;
  border-left: 15px solid transparent;
}

</style>
