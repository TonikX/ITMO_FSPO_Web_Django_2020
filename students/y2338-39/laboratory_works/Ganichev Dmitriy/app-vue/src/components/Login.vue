<template>
    <div>
        <v-form ref="formLogin" class="tform">
            <v-text-field hide-details="auto" v-model="login" type="text" label="Username" v-on:keyup.enter="!password ? $refs.txPwd.focus() : pressLogin()"/>
            <v-text-field ref="txPwd" hide-details="auto" v-model="password" type="password" label="Password" v-on:keyup.enter="pressLogin"/>
            <v-btn @click="pressLogin" class="submitbtn">Login</v-btn>
        </v-form>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        created() {
            if (localStorage.getItem("auth"))
                this.$router.replace({path: '/'});
        },
        methods: {
            pressLogin() {
                this.axios.post('http://' + this.$me.host + '/auth/token/login/',
                    {
                        username: this.login,
                        password: this.password,
                    }).then((res, b, e) => {
                        localStorage.setItem("auth", res.data.auth_token);
                        this.$emit('refreshLogin');
                    }).catch((res, d) => {
                        if (res.response.status == 400)
                            this.__alert("Login or password is incorrect");
                        else
                            this.__alert("An unknown error occured.");
                    });
            },
            __alert(text) {
              this.$emit("_alert", "Error", text);
            }
        }
    }
</script>

