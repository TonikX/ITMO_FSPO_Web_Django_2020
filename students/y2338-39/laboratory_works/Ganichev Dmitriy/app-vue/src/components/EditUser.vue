<template>
    <div>
        <v-toolbar flat class="tform">
            <span>You are:</span>
            <v-spacer></v-spacer>
            <span class="cyan--text" small>{{ $me.user.user.role.beautify() }}</span>
        </v-toolbar>
        <v-form v-if="$me.user.user.role != 'Admin'" v-model="editValid" ref="formEdit" class="tform">
            <v-toolbar flat>
                <span v-if="$me.user.user.role == 'FurFactoryManager'">Your factory name:</span>
                <span v-else>Your address:</span>
                <v-spacer></v-spacer>
                <span class="cyan--text" >{{address}}</span>
            </v-toolbar>
            <v-text-field ref="txA" v-if="$me.user.user.role != 'FurFactoryManager'" :rules="rules.required" hide-details="auto" v-model="details_a" type="text" required label="New address" v-on:keyup.enter="pressChangeA" value="this.$me.user.address" />
            <v-text-field ref="txA" v-else :rules="rules.required" hide-details="auto" v-model="details_a" type="text" required label="New factory name" v-on:keyup.enter="pressChangeA" value="this.$me.user.name" />
            <v-btn @click="pressChangeA" class="submitbtn">Change</v-btn>
        </v-form>
        <v-form v-model="editPassValid" ref="formEditPass" class="tform">
            <v-text-field :rules="rules.required" hide-details="auto" v-model="old_password" type="password" required label="Old password" />
            <v-text-field :rules="rules.passwd" hide-details="auto" v-model="new_password" type="password" required label="New password" @keyup="passConfirmCheck" />
            <v-text-field ref="txPassconfirm" :rules="rules.passconf" hide-details="auto" v-model="new_password2" type="password" required label="Confirm new password" @keyup="passConfirmCheck" />
            <v-btn @click="pressChangePassword" class="submitbtn">Change password</v-btn>
        </v-form>
    </div>
</template>

<script>
    export default {
        name: "EditUser",
        data() {
            return {
                details_a: '',
                editValid: true,

                old_password: '',
                new_password: '',
                new_password2: '',
                editPassValid: true,

                rules: {
                    required: [value => !!value || "Required."],
                    passwd: [value => !!value || "Required.", value => (value.length >= 4) || "Password must be at least 4 characters long."],
                    passconf: [value => !!value || "Required.", value => !this.new_password ||
                        this.new_password == value || "Passwords don't match."],

                },

                address: ''
            }
        },
        created() {
            var q = (this.$me.user || {});
            this.address = q.name || q.address;
        },
        methods: {
            pressChangeA() {
                this.$refs.formEdit.validate();
                if (!this.editValid)
                {
                    this.$refs.txA.focus();
                    return;
                }

                this.axios.put('http://' + this.$me.host + '/api/1/me/',
                    {
                        a: this.details_a
                    }).then((res) => {
                        if (res.data.status == "error")
                            this.$emit('_alert', "Error", res.data.data);
                        else
                        {
                            this.$emit('_alert', "Success", "Success!");
                            this.address = this.details_a;
                        }
                    }).catch((res) => {
                        this.$emit('_alert', "Error", res.response.data);
                    });
            },
            pressChangePassword(){
                this.$refs.formEditPass.validate();
                if (this.new_password2 != this.new_password)
                {
                    this.$refs.txPassconfirm.focus();
                    return;
                }
                if (!this.editPassValid) return;


                this.axios.put('http://' + this.$me.host + '/api/1/me/',
                    {
                        o: this.old_password,
                        n: this.new_password,
                        c: this.new_password2
                    }).then((res) => {
                        if (res.data.status == "error")
                            this.$emit('_alert', "Error", res.data.data);
                        else
                            this.$emit('_alert', "Success", "Password changed successfully!");
                    }).catch((res) => {
                        this.$emit('_alert', "Error", res.response.data);
                    });
            },
            passConfirmCheck() {
                this.$refs.txPassconfirm.validate();
            }
        }
    }
</script>
