<template>
    <v-container>
      <v-card
        color="#FFFFFF"
        elevation=2
        height="1400px"
        width="1188px"
        rounded="xl"
        class="bigrect"
      >
        <div>
            <v-row>
                <v-col
                class="searchtext" >
                    <h1>Filtros</h1>
                </v-col>

                <v-col
                class="searchfilter">
                    <v-select
                    :items="filtros"
                    filled
                    rounded
                    label="Filtro 1"
                    style="width:200px"
                    v-model="interest"
                    v-on:change="searchFilter"
                    ></v-select>
                </v-col>

            </v-row>

            <v-row>
              <v-divider intern class="divider"></v-divider>
            </v-row>

            <v-row
                v-for="(item) in toRender" :key="item.group_name"
                class="groupcards"
            >
                    <v-card
                        :color="cor"
                        dark
                        height="200px"
                        width="1000px"
                    >
                      <v-row>
                        <v-column>
                          <v-img src= '../assets/landscape.jpeg'
                          height="150px"
                          width="150px"
                          class="cardimage"
                          ></v-img>
                        </v-column>
                        <v-column>
                          <v-row>
                              <h2 class="cardcontent">{{ item.group_name }}</h2>
                          </v-row>
                          <v-row>
                            <div class="cardtext">
                              {{ item.about }}
                            </div>
                          </v-row>
                          <v-row>
                            <v-column>
                              <v-btn class="cardcontent">
                                enter
                              </v-btn>
                            </v-column>
                          </v-row>
                        </v-column>
                      </v-row>
                    </v-card>
            </v-row>
            <v-row>
              <v-divider intern class="divider"></v-divider>
            </v-row>

            <v-row v-if="toRender.length > 4">
                <v-btn @click="loadnext()" class="nextbutton">next</v-btn>
            </v-row>
        </div>
      </v-card>
    </v-container>
  </template>
  
  <script>
    import axios from 'axios';

    export default {
        data: () => ({
            filtros: ['Ciencia', 'Historia', 'Portugues', 'Matematica', 'Geografia', 'Politica', 'Computacao', 'Filosofia', 'Sociologia'],
            cor: '#D9D9D9',
            interest: "Ciencia",
            start: 0, // Lower limit 
            end: 5, // Upper Limit
            allGroups: [],
            toRender: []
        }),

        async mounted() {
          let url = 'http://localhost:8890/getGroupInterest'

          const data = {
            interest: this.interest
          };

          const response = await axios.post(url,data, {headers:{'Access-Control-Request-Method': 'POST'}}).then(response => response.data)
          this.allGroups = response
          this.end = this.allGroups.length
          for (let i = this.start; i < (this.start + 5); i++){
              if (i >= this.end) {
                break;
              }
              this.toRender.push(this.allGroups[i])
          }

          this.start = this.start + this.toRender.length
        },

        methods: {
            loadnext() {
              this.toRender = [];
              for (let i = this.start; i < (this.start + 5); i++){
                  if (i >= this.end) {
                    break;
                  }
                  this.toRender.push(this.allGroups[i])
              }
              this.start += 5
            },
            async searchFilter() {
              let url = 'http://localhost:8890/getGroupInterest'

              const data = {
                interest: this.interest
              };

              this.start = 0
              this.toRender = []
              const response = await axios.post(url,data, {headers:{'Access-Control-Request-Method': 'POST'}}).then(response => response.data)
              this.allGroups = response
              this.end = this.allGroups.length
              for (let i = this.start; i < (this.start + 5); i++){
                  if (i >= this.end) {
                    break;
                  }
                  this.toRender.push(this.allGroups[i])
              }

              this.start = this.start + this.toRender.length
            }
        } 
    }
  </script>

  <style>
  .searchtext {
    border-right: 70px solid transparent;
    border-left: 70px solid transparent;
    border-top: 50px solid transparent;
  }

  .searchfilter {
    border-right: 0px solid transparent;
    border-left: 30px solid transparent;
    border-top: 50px solid transparent;
  }

  .groupcards {
    border-right: 70px solid transparent;
    border-left: 70px solid transparent;
    border-top: 20px solid transparent;
  }
  
  .buttonregister {
    background-color: #0D1A8F;
    color: white;
  }
  
  .bigrect {
    margin-top: 30px;
    margin-bottom: 20px;
    margin-left: -5px;
  }
  
  .uploading-image{
       display:flex;
     }

  .divider {
      margin-top: 15px;
      margin-left: 50px;
      margin-right: 50px;
  }

  .cardimage {
    margin-top: 30px;
    margin-left: 50px;
    margin-right: 50px;
  }

  .cardcontent {
    color:#000000;
    margin-top: 50px;
    margin-left: 50px;
    margin-right: 50px;
    margin-bottom: 10px;
  }

  .cardtext {
    color:#000000;
    margin-left: 50px;
    margin-right: 50px;
    margin-bottom: 10px;
  }

  .nextbutton {
    margin-top: 50px;
    margin-left: 50px;
    margin-right: 50px;
    margin-bottom: 50px;
  }
  </style>
  
