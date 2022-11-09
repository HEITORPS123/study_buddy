<template>
  <v-dialog
    transition="dialog-bottom-transition"
    width="auto"
    height="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn 
        class="mt-8"
        color="blue"
        v-bind="attrs"
        v-on="on"
      >
        <h3> Criar Evento </h3>
      </v-btn>
    </template>
    <template v-slot:default="dialog">
      <v-card
        width="450px"
        height="600px"
      >
        <v-row>
          <v-col>
            <h2 class="ma-5"> Criar Evento </h2>
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
          <v-text-field
          class="ml-12"
          label="Nome do Evento"
          ref="event_name"
          v-model="event_name"
          filled
          clearable
          rounded
          >
          </v-text-field>
          <v-spacer/>
        </v-row>

        <v-row>
          <v-text-field
          class="ml-12"
          label="Data do Evento"
          ref="event_date"
          v-model="event_date"
          filled
          clearable
          rounded
          >
          </v-text-field>
          <v-spacer/>
        </v-row>

        <v-row>
          <v-textarea
          class="event-about-create"
          label="Informações sobre o evento"
          v-model="event_about"
          height="210px"
          rounded
          clearable
          filled
          ></v-textarea>
          <v-spacer/>
        </v-row>

        <v-row>
          <v-spacer/>
          <v-btn
            class="mt-2"
            color="blue"
            @click="create();dialog.value=false"
          >
            <h3> Criar </h3>
          </v-btn>
          <v-spacer/>
        </v-row>

      </v-card>
    </template>
  </v-dialog>
</template>
<script>
import axios from 'axios';
export default {
  methods: {
    async create () {
      let url = 'http://localhost:8890/createEvent'
      let data = {
          group_id: parseInt(this.$route.params.group_id),
          event_name: this.event_name,
          content: this.event_about,
          date: this.event_date
      }
      console.log(data)
      await axios.post(url,data)
    }
  }
}
</script>
<style>
.event-about-create {
  width: 270px;
  margin-left: 50px !important;
}
</style>
