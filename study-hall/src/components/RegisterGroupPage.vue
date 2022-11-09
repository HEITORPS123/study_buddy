<template>
  <v-container>
    <v-card
      color="#FFFFFF"
      elevation=2
      height="800px"
      width="1188px"
      rounded="xl"
      class="bigrect-register-group"
    >
      <div>
        <v-row>
          <v-col
          cols="12"
          lg="8"
          class="pa-8" >
            <h1>Register Group</h1>
          </v-col>
        </v-row>
      </div>

      <v-row no-gutters>
        <v-col
        cols="12"
        lg="6"
        class="pa-8" >
          <v-text-field filled label="Group Name" v-model="group_name"></v-text-field>
        </v-col>
        <v-spacer></v-spacer>
        <v-col
        cols="12"
        lg="6"
        class="pa-8" >
          <v-select
            :items="items"
            filled
            label="Group's Subjects"
            v-model="interest"
          ></v-select>
        </v-col>
      </v-row>

      <v-row
        :align="align"
        no-gutters >
        <v-col
          cols="12"
          lg="6"
          class="pa-8" >
          <v-text-field filled label="Organizer Name" v-model="organizer_name"></v-text-field>
        </v-col>
        <v-spacer></v-spacer>
        <v-col
          cols="12"
          lg="6"
          class="pa-8" >
            <v-text-field filled label="Organizer Contact" v-model="organizer_contact"></v-text-field>
        </v-col>
      </v-row>

      <v-row
        :align="align"
        no-gutters >
       <v-col class="pa-8" >
          <v-textarea
           filled
           label="About Group"
           v-model="aboutMeContent"
           height="200px"></v-textarea>
         </v-col>
       </v-row>

      <div class="text-center">
         <v-btn
           height=84
           width=266
           color="primary"
           @click="postFormGrupo"
         >
         Register
         </v-btn>
      </div>
    </v-card>
  </v-container>
</template>

<script>
  import axios from 'axios';

  export default {
    data: () => ({
      items: ['Ciencia', 'Historia', 'Portugues', 'Matematica', 'Geografia', 'Politica', 'Computacao', 'Filosofia', 'Sociologia'],
      group_name: "",
      organizer_name: "",
      organizer_contact: "",
      interest: "",
      aboutMeContent: ""      
    }),

    methods: {
      async postFormGrupo() {
        let url = 'http://localhost:8890/createGroup'
        let user_id = document.cookie.split('=')[1]
        const data = {
          user_id: parseInt(user_id),
          group_name: this.group_name,
          organizer_name: this.organizer_name,
          organizer_contact: this.organizer_contact,
          interest: this.interest,
          about: this.aboutMeContent
        };

        await axios.post(url, data, {headers: {'Access-Control-Request-Method': 'POST'}})
        this.$router.push('/')
      },
    }
  }
</script>

<style>
.hometext-register-group {
  border-right: 70px solid transparent;
  border-left: 70px solid transparent;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

.buttonregister-register-group {
  background-color: #0D1A8F;
  color: white;
}

.bigrect-register-group {
  margin-top: 30px;
  margin-bottom: 20px;
  margin-left: -5px;
}

.uploading-image{
     display:flex;
   }
</style>
