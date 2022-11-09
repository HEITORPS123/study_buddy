<template>
  <v-dialog
    transition="dialog-bottom-transition"
    width="auto"
    height="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        class="group-name-buttons"
        color="blue"
        text
        outlined
        flatten
        v-bind="attrs"
        v-on="on"
      >
        <h3>Ver Eventos</h3>
      </v-btn>
    </template>
    <template v-slot:default="dialog">
      <v-card
        width="670px"
        height="600px"
      >
        <v-row>
          <v-col>
            <h2 class="ma-5"> Eventos do Grupo </h2>
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
          <v-sheet
            class="ma-auto"
            outlined
            rounded
            elevation="3"
          >
            <v-responsive
              class="overflow-y-auto"
              width="600px"
              height="400px"
            >
              <v-row
                v-for="(event) in events" :key="events.findIndex(x=>x==event)"
              >
                <v-card
                  class="pa-6"
                  height="auto"
                  width="600px"
                >
                  <v-row>
                    <v-row>
                      <v-col>
                      <b class="event-name"> {{ event.event_name }} </b>
                      </v-col>
                      <v-col>
                      <p> {{ event.date }} </p>
                      </v-col>
                    </v-row>
                    <v-row>
                      <p class="event-about"> {{ event.about }} </p>
                    </v-row>
                  </v-row>
                </v-card>
              </v-row>
            </v-responsive>
          </v-sheet>
        </v-row>

        <v-row>
          <v-spacer/>
          <GroupCreateEvents/>
          <v-spacer/>
        </v-row>

      </v-card>
    </template>
  </v-dialog>
</template>
<script>
import axios from 'axios';
import GroupCreateEvents from "@/components/GroupCreateEventsComponent";
export default {
  components: {
    GroupCreateEvents
  },
  data: () => ({
    events: []
  }),
  async mounted () {
      let url = 'http://localhost:8890/getEventGroup'
      let data = {
          id: parseInt(this.$route.params.group_id),
      }

      const response = await axios.post(url,data)
      this.events = response.data
  }
}
</script>
<style>
.event-name {
  padding-top: 46px;
  padding-bottom: 16px;
  padding-left: 16px;
  padding-right: 16px;
}

.event-about {
  padding-top: 2px;
  padding-bottom: 8px;
  padding-left: 28px;
  padding-right: 8px;
}
</style>
