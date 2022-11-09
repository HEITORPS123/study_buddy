<template>
  <v-container>
    <v-card
      color="#FFFFFF"
      elevation=2
      height="975px"
      width="1188px"
      rounded="xl"
      class="bigrect-register"
    >
      <div>
        <v-row>
          <v-col
          cols="12"
          lg="8"
          class="pa-8" >
            <h1>Register</h1>
          </v-col>
        </v-row>
      </div>

      <v-row no-gutters>
        <v-col
        cols="12"
        lg="6"
        class="pa-8" >
          <v-text-field filled label="Username" v-model="username"></v-text-field>
        </v-col>
        <v-spacer></v-spacer>
        <v-col
        cols="12"
        lg="6"
        class="pa-8" >
          <v-select
            :items="items"
            filled
            label="Interests"
            multiple
            v-model="itemsSelected"
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
          <v-text-field filled label="Password" type="password" v-model="password"></v-text-field>
        </v-col>
        <v-spacer></v-spacer>
        <v-col
          cols="12"
          lg="6"
          class="pa-8" >
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="computedDateFormatted"
                  filled
                  label="Birthday"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="date"
                no-title
                @input="menu2 = false"
              ></v-date-picker>
            </v-menu>
        </v-col>
      </v-row>

      <v-row
        :align="align"
        no-gutters >
        <v-col
          class="pa-8" >
          <v-text-field filled label="Full Name" v-model="fullName"></v-text-field>
        </v-col>
      </v-row>

      <v-row
        :align="align"
        no-gutters >
       <v-col class="pa-8" >
          <v-textarea
           filled
           label="About me"
           height="200px"
           v-model="aboutMeContent"></v-textarea>
         </v-col>
       </v-row>

      <div class="text-center">
         <v-btn
           height=84
           width=266
           color="primary"
           @click="postForm"
         >
         Register
         </v-btn>
      </div>
    </v-card>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      items: ['Ciencia', 'Historia', 'Portugues', 'Matematica', 'Geografia', 'Politica', 'Computacao', 'Filosofia', 'Sociologia'],
    }),
  }
</script>

<script>
  import axios from 'axios';
  
  export default {
    data: vm => ({
      items: ['Ciencia', 'Historia', 'Portugues', 'Matematica', 'Geografia', 'Politica', 'Computacao', 'Filosofia', 'Sociologia'],
      date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      dateFormatted: vm.formatDate((new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10)),
      menu1: false,
      menu2: false,
      itemsSelected: [],
      interests: "",
      username: "",
      password: "",
      fullName: "",
      aboutMeContent: ""
    }),

    computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },

    watch: {
      date (val) {
        this.dateFormatted = this.formatDate(this.date)
      },
    },

    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${month}/${day}/${year}`
      },
      parseDate (date) {
        if (!date) return null

        const [month, day, year] = date.split('/')
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
      },
      async postForm() {
        let url = 'http://localhost:8890/createUser'

        this.interests = this.itemsSelected.join('-')
        const data = {
          username: this.username,
          interests: this.interests,
          password: this.password,
          birthday: this.dateFormatted,
          fullname: this.fullName,
          about: this.aboutMeContent
        };

        const response = await axios.post(url,data, {headers:{'Access-Control-Request-Method': 'POST'}})
        this.$router.push('/')
      },
    }
  }
</script>

<style>
.hometext-register {
  border-right: 70px solid transparent;
  border-left: 70px solid transparent;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

.buttonregister-register {
  background-color: #0D1A8F;
  color: white;
}

.bigrect-register {
  margin-top: 30px;
  margin-bottom: 20px;
  margin-left: -5px;
}

.uploading-image{
     display:flex;
   }
</style>
