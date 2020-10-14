<template>
  <v-app dark>
    <v-app-bar
      app
    >
      <v-btn :to="{path: '/'}" text>Home</v-btn>
      <v-row justify="center">
         <v-dialog
           v-model="alertDialog"
           max-width="350"
         >
          <v-card>
            <v-card-title class="headline">
              {{alertTitle}}
            </v-card-title>
            <v-card-text>{{alertText}}</v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="gray"
                text
                @click="alertDialog = false;"
              >
                OK
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
      <v-spacer></v-spacer>
      <v-btn v-if="!auth" :to="{path: '/login'}" style="margin: 0 16px">Log in</v-btn>
      <v-btn v-if="!auth" :to="{path: '/reg'}">Register</v-btn>
      <v-row v-if="auth">
        <v-spacer></v-spacer>
        <div class="v-btn v-btn--flat v-btn--text v-size--default welcome" v-if="show">
          <span class="v-btn__content">Welcome, {{$me.user.user.username}}!&nbsp;</span>
        </div>
        <v-btn :to="{path: '/edit'}">Profile</v-btn>
        <v-dialog
          v-model="logoutDialog"
          persistent
          max-width="350"
        >
          <template v-slot:activator="{ on, attrs }">
              <v-btn
                v-bind="attrs"
                v-on="on"
                style="margin: 0 16px"
              >
                Logout
              </v-btn>
          </template>
          <v-card>
              <v-card-title class="headline">
                Confirmation
              </v-card-title>
              <v-card-text>Are you sure want to logout?</v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="gray"
                  text
                  @click="logoutDialog = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="red darken-1"
                  text
                  @click="logoutDialog = false; goLogout()"
                >
                  Proceed
                </v-btn>
              </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
      <v-btn @click="$me.settings.self.theme.dark = ($vuetify.theme.dark = !$vuetify.theme.dark); $me.settings.save()" text fab small style="margin: 0 0 0 16px">
        <v-icon v-if="$vuetify.theme.dark">mdi-white-balance-sunny</v-icon>
        <v-icon v-else>mdi-moon-waxing-crescent</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <div style="height: 20px"></div>
      <router-view v-if="show" v-on:refreshLogin="refresh" v-on:_alert="alert"></router-view>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    created() {
      this.refresh()
    },
    components: {
    },
    computed: {
      auth() {
        return localStorage.getItem('auth');
      },
      show() {
        return !localStorage.getItem('auth') || !!(this.$me.user && this.$me.user.user);
      }
    },
    methods: {
        goLogout() {
          delete this.$me.user;
          this.reshow();
          setImmediate(() => {
            localStorage.removeItem('auth');
            this.refresh();
          });
        },
        refresh() {
          if (localStorage.getItem('auth'))
          {
            this.reshow();
            this.axios.defaults.headers.common['Authorization'] = 'Token ' + localStorage.getItem("auth");
            if (!this.$me.user)
              this.axios.get('http://' + this.$me.host + '/api/1/me/')
                .then((res) => {
                  this.$me.user = res.data.data;
                  this.reshow();
                }).catch((res) => {
                  this.goLogout();
                });
          }
          else
          {
            this.axios.defaults.headers.common['Authorization'] = '';
            this.reshow();
          }
        },
        reshow() {
          if (this.show && 
            (!this.$me.user && ['/', '/login', '/reg'].indexOf(this.$router.currentRoute.path) === -1) ||
            (this.auth && ['/login', '/reg'].indexOf(this.$router.currentRoute.path) !== -1))
            this.$router.replace({path: '/'});
          this.$forceCompute('auth', false);
          this.$forceCompute('show');
        },
        alert(title, text)
        {
          this.alertTitle = title;
          this.alertText = text;
          this.alertDialog = true;
        }
    },
    data: () => ({
      logoutDialog: false,
      alertDialog: false,
      alertTitle: '',
      alertText: '',
    }),
  };
</script>
