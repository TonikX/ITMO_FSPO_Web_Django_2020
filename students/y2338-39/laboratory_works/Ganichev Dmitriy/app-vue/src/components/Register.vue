<template>
    <div>
        <v-form v-model="reg_valid" ref="formReg" class="tform">
            <v-combobox :rules="rules.required" hide-details="auto" v-model="r" :items="items" label="Register as" required placeholder="Select..."/>
            <v-text-field ref="txUsername" :rules="rules.username" hide-details="auto" v-model="u" type="text" required label="Username" @keyup="usernameCheck"/>
            <v-text-field :rules="rules.passwd" hide-details="auto" v-model="p" type="password" required label="Password" @keyup="passConfirmCheck"/>
            <v-text-field ref="txPassconfirm" :rules="rules.passconf" hide-details="auto" v-model="c" type="password" required label="Confirm password" @keyup="passConfirmCheck"/>
            <v-text-field :rules="rules.required" v-if="this.r==this.items[2]" hide-details="auto" v-model="a" required type="text" label="Factory name"/>
            <v-text-field :rules="rules.required" v-else hide-details="auto" v-model="a" type="text" required label="Address"/>
            <v-btn @click="pressRegister" class="submitbtn">Register</v-btn>
        </v-form>
    </div>
</template>

<script>
    export default {
        name: "Login",
        created() {
            if (localStorage.getItem("auth"))
                this.$router.replace({path: '/'});
        },
        data() {
            return {
                u: '',
                p: '',
                c: '',
                r: '',
                a: '',
                reg_valid: false,
                un_available: true,

                items: [
                    'Hunter',
                    'Fur Point Worker',
                    'Fur Factory Manager',
                ],

                rules: {
                    required: [value => !!value || "Required."],
                    username: [value => !!value || "Required.", value => this.un_available || "Username is not available"],
                    passwd: [value => !!value || "Required.", value => (value.length >= 4) || "Password must be at least 4 characters long."],
                    passconf: [value => !!value || "Required.", value => !this.p || value == this.p || "Passwords don't match."],
                }
            }
        },
        methods: {
            pressRegister() {
                this.$refs.formReg.validate();
                if (!this.un_available) 
                {
                    this.$refs.txUsername.focus();
                    return;
                }
                if (this.c != this.p)
                {
                    this.$refs.txPassconfirm.focus();
                    return;
                }
                if (!this.reg_valid) return;

                this.axios.post('http://' + this.$me.host + '/api/1/register/',
                    {
                        u: this.u,
                        p: this.p,
                        c: this.c,
                        r: {[this.items[0]]: 'H', [this.items[1]]: 'W', [this.items[2]]: 'F'}[this.r],
                        a: this.a
                    }).then((res) => {
                        if (res.data.status == "error")
                            this.$emit("_alert", "Error", "An error occured: " + res.data.data);
                        else
                        {
                            this.$router.push({name: 'login'});
                            this.$emit("_alert", "Success", "You were successfully registered, you may now login with your new credentials.");
                        }
                    }).catch((res) => {
                        this.$emit("_alert", "Error", "An error occured!");
                    });
            },
            usernameCheck() {
                if (!this.u)
                {
                    this.un_available = true;
                }
                else
                {
                    var un = this.u;
                    this.axios.get('http://' + this.$me.host + '/api/1/check/?u=' + this.u)
                        .then((res) => {
                            if (un != this.u) return;
                            this.un_available = res.data.available;
                            this.$refs.txUsername.validate();
                        });
                }
            },
            passConfirmCheck() {
                this.$refs.txPassconfirm.validate();
            }
        }
    }
</script>
