<template>
    <v-container>
        <v-container v-if="authed && roleid != 'Admin'">
            <v-toolbar flat>
                    <span>You are:</span>
                    <v-spacer></v-spacer>
                    <span class="cyan--text" small>{{ roleid.beautify() }}</span>
            </v-toolbar>
            <v-toolbar flat v-if="earns>=0">
                    <span>Total earned:</span>
                    <v-spacer></v-spacer>
                    <span class="green--text" small>{{ earns }} ₪</span>
            </v-toolbar>
            <v-toolbar flat v-else>
                    <span>Total spent:</span>
                    <v-spacer></v-spacer>
                    <span class="red--text" small>{{ -earns }} ₪</span>
            </v-toolbar>
            <v-data-table
                    :headers="tbl_headers"
                    :items="items"
                    :items-per-page="-1"
                    hide-default-footer
                    >
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title v-if="roleid=='Hunter'">Gathered fur</v-toolbar-title>
                            <v-toolbar-title v-else-if="roleid=='FurPointWorker'">Fur received from hunters</v-toolbar-title>
                            <v-toolbar-title v-else>Fur received from fur points</v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-dialog
                                v-model="gatherDialog"
                                max-width="500px"
                                v-if="roleid==='Hunter'"
                                >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn
                                        v-bind="attrs"
                                        v-on="on"
                                        >
                                    Gather more
                                    </v-btn>
                                </template>
                                <v-card>
                                    <v-card-title>
                                        <span class="headline">Gather more fur</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-container>
                                            <v-form ref="formGather" v-model="form_valid">
                                                <v-row>
                                                    <v-col cols="12" sm="12" md="12">
                                                        <v-text-field ref="txType" :rules="rules.required" hide-details="auto" v-model="type" type="text" required label="Fur type" />
                                                    </v-col>
                                                    <v-col cols="12" sm="6" md="6">
                                                        <v-combobox :rules="rules.sort" hide-details="auto" v-model="sort" :items="sorts" label="Fur sort" required placeholder="Select..."/>
                                                    </v-col>
                                                    <v-col cols="12" sm="6" md="6">
                                                        <v-input-number :rules="rules.count" hide-details="auto" v-model="count" label="Count" required value=1 :min=1></v-input-number>
                                                    </v-col>
                                                </v-row>
                                            </v-form>
                                        </v-container>
                                    </v-card-text>

                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn
                                            text
                                            @click="gatherDialog=false;"
                                        >
                                            Cancel
                                        </v-btn>
                                        <v-btn
                                            text
                                            @click="pressAdd();"
                                        >
                                            Gather!
                                        </v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                        </v-toolbar>
                    </template>
                    <template v-slot:item.id_hunter="{ item }">
                        <v-btn text v-on:click='showDetails("h", item.id_hunter)'>{{item.id_hunter}}</v-btn>
                    </template>
                    <template v-slot:item.id_fufurpoint="{ item }">
                        <v-btn text v-on:click='showDetails("w", item.id_furpoint)'>{{item.id_furpoint}}</v-btn>
                    </template>
            </v-data-table>
            <v-data-table
                :headers="tbl_headersout"
                :items="sends"
                hide-default-footer
                v-if="roleid!=='FurFactoryManager'"
                :items-per-page="-1"
                >
                <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title v-if="roleid==='Hunter'">Fur sent to points</v-toolbar-title>
                            <v-toolbar-title v-else>Fur sent to factories</v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-dialog
                                v-model="sendDialog"
                                max-width="500px"
                                >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn
                                        v-bind="attrs"
                                        v-on="on"
                                        >
                                    Send
                                    </v-btn>
                                </template>
                                <v-card>
                                    <v-card-title>
                                        <span v-if="roleid==='Hunter'" class="headline">Send to fur point</span>
                                        <span v-else class="headline">Send to fur factory</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-container>
                                            <v-form ref="formSend" v-model="form_valid">
                                                <v-row>
                                                    <v-col cols="12" sm="12" md="12">
                                                        <v-combobox ref="txSendType" :rules="rules.typesend" hide-details="auto" v-model="type" :items="typesSend" type="text" required label="Fur type" />
                                                    </v-col>
                                                    <v-col cols="12" sm="6" md="6">
                                                        <v-combobox :rules="rules.sortsend" hide-details="auto" v-model="sort" :items="sortsSend" label="Fur sort" required placeholder="Select..."/>
                                                    </v-col>
                                                    <v-col cols="12" sm="4" md="4">
                                                        <v-input-number :rules="rules.countsend" hide-details="auto" v-model="count" label="Count" required value=1 :min=1></v-input-number>
                                                    </v-col>
                                                    <v-col cols="12" sm="2" md="2">
                                                        <div class="v-btn v-btn--flat v-btn--text v-size--default" style="margin: 16px 0">/ {{countSend}}</div>
                                                    </v-col>
                                                    <v-col cols="12" sm="12" md="12">
                                                        <v-combobox v-if="roleid==='Hunter'" :rules="rules.points" hide-details="auto" v-model="to" :items="pointsCbx" type="text" required label="Fur point" />
                                                        <v-combobox v-else :rules="rules.factories" hide-details="auto" v-model="to" :items="factoriesCbx" type="text" required label="Fur factory" />
                                                    </v-col>
                                                    <v-col cols="12" sm="12" md="12">
                                                        <v-input-number :rules="rules.price" hide-details="auto" v-model="price" label="Price" required :min=1></v-input-number>
                                                    </v-col>
                                                </v-row>
                                            </v-form>
                                        </v-container>
                                    </v-card-text>

                                    <v-card-actions>
                                        <v-spacer></v-spacer>
                                        <v-btn
                                            text
                                            @click="sendDialog=false;"
                                        >
                                            Cancel
                                        </v-btn>
                                        <v-btn
                                            text
                                            @click="pressSend();"
                                        >
                                            Send
                                        </v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-dialog>
                        </v-toolbar>
                </template>
                <template v-slot:item.id_furfactory="{ item }">
                    <v-btn text v-on:click='showDetails("f", item.id_furfactory)'>{{item.id_furfactory}}</v-btn>
                </template>
                <template v-slot:item.id_furpoint="{ item }">
                    <v-btn text v-on:click='showDetails("w", item.id_furpoint)'>{{item.id_furpoint}}</v-btn>
                </template>
            </v-data-table>
            <v-dialog
                v-model="detailsDialog"
                max-width="350px"
                >
                <v-card>
                    <v-card-title>
                        <span class="headline">{{details.name}}</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <span>{{details.uname_name}}:</span>
                                <v-spacer></v-spacer>
                                <span>{{details.uname_value}}</span>
                            </v-row>
                            <v-row>
                                <span>{{details.data_name}}:</span>
                                <v-spacer></v-spacer>
                                <span>{{details.data_value}}</span>
                            </v-row>
                        </v-container>
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            text
                            @click="detailsDialog=false;"
                        >
                            OK
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-container>
        <v-container v-else-if="authed && roleid == 'Admin'">
            <v-data-table
                :headers="tbl_headersadmin"
                :items="admusers"
                :custom-sort="customSort"
                :footer-props="{
                    'items-per-page-options': [10, 20, 50, -1]
                }"
                >
                <template v-slot:top>
                    <v-toolbar flat>
                        <v-toolbar-title>System users</v-toolbar-title>
                        <v-spacer></v-spacer>
                    </v-toolbar>
                </template>
                <template v-slot:item.role="{ item }">
                    {{ item.role.beautify() }}
                </template>
                <template v-slot:item.earn="{ item }">
                    <span v-if="item.role == 'Admin'" class="orange--text">—</span>
                    <span v-else-if="earned(item)>=0" class="green--text">{{ earned(item) }} ₪</span>
                    <span v-else class="red--text">{{ earned(item) }} ₪</span>
                </template>
            </v-data-table>
        </v-container>
        <v-container v-else>
            <v-card>
                <v-card-title>
                    HUNTERS system
                </v-card-title>
                <v-card-text>
                    <strong>Welcome, stranger!</strong> We are happy that you found our site on the internet! Here you may gather, send and deliver fur and get money!<br/>
                    <i>To begin, press login or register</i>
                </v-card-text>
            </v-card>
        </v-container>
    </v-container>
</template>

<script>
    export default {
        name: "Main",
        data() {
            return {
                type: '',
                sort: 0,
                count: 1,
                to: '',
                price: '',

                form_valid: true,
                items: [],
                sends: [],
                admsends: [],
                admusers: [],
                hunters: {},
                points: {},
                factories: {},

                sorts: [
                    '1', '2', '3'
                ],

                interval: '',

                rules: {
                    required: [value => !!value || "Required."],
                    sort: [value => !!value || "Required.", value => value > 0 && value < 4 || "Invalid sort"],
                    count: [value => !!value || "Required.", value => parseInt(value) > 0 || "Count must be positive"],
                    price: [value => !!value || "Required.", value => parseInt(value) > 0 || "Price must be positive"],
                    typesend: [value => !!value || "Required.", value => this.typesSend.indexOf(value) !== -1 || "You don't own this fur type"],
                    sortsend: [value => !!value || "Required.", value => this.sortsSend.indexOf(value) !== -1 || "You don't own this fur sort"],
                    countsend: [value => !!value || "Required.", value => parseInt(value) > 0 || "Count must be positive", value => parseInt(value) <= this.countSend || "You don't have such fur count"],
                    points: [value => !!value || "Required.", value => this.pointsCbx.indexOf(value) !== -1 || "Invalid point selected."],
                    factories: [value => !!value || "Required.", value => this.factoriesCbx.indexOf(value) !== -1 || "Invalid factory selected."],
                },

                tbl_headers: [
                    {text: 'Fur type', value: 'type'},
                    {text: 'Fur sort', value: 'sort'},
                    {text: 'Count', value: 'count'},
                    {text: 'Gather date', value: 'date'},
                ],
                tbl_headersout: [
                    {text: 'Fur type', value: 'type'},
                    {text: 'Fur sort', value: 'sort'},
                    {text: 'Count', value: 'count'},
                    {text: 'Price', value: 'price'},
                    {text: 'Send date', value: 'date'},
                ],
                tbl_headersadmin: [
                    {text: 'ID', value: 'id'},
                    {text: 'Username', value: 'username'},
                    {text: 'Role', value: 'role'},
                    {text: 'Total earns', value: 'earn', align: 'end'},
                ],

                gatherDialog: false,
                sendDialog: false,
                detailsDialog: false,

                details: {
                    name: '',
                    uname_name: '',
                    uname_value: '',
                    data_name: '',
                    data_value: '',
                }
            }
        },
        computed: {
            pointsCbx() {
                return Object.values(this.points).map(x => 'Point ' + x.id + " at " + x.address + " (worker " + x.user.username + ")");
            },
            factoriesCbx() {
                return Object.values(this.factories).map(x => 'Factory ' + x.id + " named " + x.name + " (manager " + x.user.username + ")")
            },

            typesSend() {
                return Array.from(new Set(this.items.map(x => x.type)));
            },
            sortsSend() {
                return Array.from(new Set(this.items.filter(x => x.type == this.type).map(x => x.sort)))
            },
            countSend() {
                return this.items.filter(x => x.sort == this.sort && x.type == this.type)
                        .reduce((a, v) => a + v.count, 0) -
                    this.sends.filter(x => x.sort == this.sort && x.type == this.type)
                        .reduce((a, v) => a + v.count, 0);
            },
            earns() {
                return this.sends.reduce((a, v) => a + (v.price || 0) * v.count, 0) -
                       this.items.reduce((a, v) => a + (v.price || 0) * v.count, 0);
            },
            roleid() {
                return this.authed ? this.$me.user.user.role : null;
            },
            authed() {
                return !!this.$me.user;
            },
        },
        created() {
            if (!this.authed) return;
            if (this.roleid == "Hunter")
                this.tbl_headersout.unshift({text: 'Point', value: 'id_furpoint'});
            if (this.roleid == "FurPointWorker")
            {
                this.tbl_headersout.unshift({text: 'Factory', value: 'id_furfactory'});
                this.tbl_headers.unshift({text: "Hunter", value: 'id_hunter'});
                this.tbl_headers.insert(4, {text: 'Price', value: 'price'});
            }
            this.load();
            clearInterval(this.interval);
            this.interval = setInterval(() => this.load(), 5000);
        },
        destroyed() {
            clearInterval(this.interval);
        },
        methods: {
            load() {
                this.axios.get("http://" + this.$me.host + "/api/1/me/data/")
                    .then((res) => {
                        this.items = res.data.datain;
                        this.sends = res.data.dataout;
                        this.admsends = res.data.dataadm;
                        this.admusers = res.data.users;
                    });
                this.axios.get("http://" + this.$me.host + "/api/1/hunters/")
                    .then((res) => {
                        this.hunters = Object.fromEntries(res.data.map(x => [x.id, x]));
                    });
                this.axios.get("http://" + this.$me.host + "/api/1/furpoints/")
                    .then((res) => {
                        this.points = Object.fromEntries(res.data.map(x => [x.id, x]));
                    });
                this.axios.get("http://" + this.$me.host + "/api/1/furfactories/")
                    .then((res) => {
                        this.factories = Object.fromEntries(res.data.map(x => [x.id, x]));
                    });
            },
            pressAdd() {
                this.$refs.formGather.validate();
                if (!this.type) 
                {
                    this.$refs.txType.focus();
                    return;
                }
                if (!this.form_valid) return;
                this.axios.post("http://" + this.$me.host + "/api/1/me/data/", 
                    {
                        out: false,
                        type: this.type,
                        sort: this.sort,
                        count: this.count,
                    })
                    .then((res) => {
                        this.load();
                    })
                this.gatherDialog = false;
            },
            pressSend() {
                this.$refs.formSend.validate();
                if (!this.type || this.typesSend.indexOf(this.type) === -1)
                {
                    this.$refs.txSendType.focus();
                    return;
                }
                if (!this.form_valid) return;

                this.axios.post("http://" + this.$me.host + "/api/1/me/data/", 
                    {
                        out: true,
                        type: this.type,
                        sort: this.sort,
                        count: this.count,
                        price: this.price,
                        to: this.to.split(' ')[1]
                    })
                    .then((res) => {
                        this.load();
                    })
                this.sendDialog = false;
            },
            showDetails(t, i) {
                var e = {'f': this.factories, 'w': this.points, 'h': this.hunters}[t][i];
                this.details.name = {'f': 'Factory', 'w': 'Fur point', 'h': 'Hunter'}[t] + " " + e.id;
                this.details.uname_name = {'f': 'Manager', 'w': 'Worker', 'h': 'Hunter'}[t] ;
                this.details.uname_value = e.user.username;
                this.details.data_name = t == 'f' ? "Name" : "Address";
                this.details.data_value = e[t == 'f' ? "name" : "address"];
                this.detailsDialog = true;
            },
            earned(item) {
                var role = item.role;
                switch (role)
                {
                    case 'Admin':
                        return 0;
                    case 'Hunter':
                        var el = Object.values(this.hunters).filter(x => x.user.id == item.id)[0];
                        return this.sends.filter(x => x.id_hunter == el.id).reduce((a, v) => a + (v.price || 0) * v.count, 0) -
                            this.items.filter(x => x.id_hunter == el.id).reduce((a, v) => a + (v.price || 0) * v.count, 0);
                    case 'FurPointWorker':
                        var el = Object.values(this.points).filter(x => x.user.id == item.id)[0];
                        return this.admsends.filter(x => x.id_furpoint == el.id).reduce((a, v) => a + (v.price || 0) * v.count, 0) -
                            this.sends.filter(x => x.id_furpoint == el.id).reduce((a, v) => a + (v.price || 0) * v.count, 0);
                    case 'FurFactoryManager':
                        var el = Object.values(this.factories).filter(x => x.user.id == item.id)[0];
                        return -this.admsends.filter(x => x.id_furfactory == el.id).reduce((a, v) => a + (v.price || 0) * v.count, 0);
                }
                return 0;
            },
            customSort(items, index, isDesc) {
                items.sort((a, b) => {
                    if (!index[0])
                        return (a.id - b.id);
                    else if (index[0] == "earn") {
                        if (isDesc[0]) {
                            return this.earned(a) - this.earned(b);
                        } else {
                            return this.earned(b) - this.earned(a);
                        }
                    } else if (!(isNaN(a[index[0]]))) {
                        if (!isDesc[0]) {
                            return (a[index[0]] - b[index[0]]);
                        } else {
                            return (b[index[0]] - a[index[0]]);
                        }

                    } else {
                        if (!isDesc[0]) {
                            return (a[index[0]] < b[index[0]]) ? -1 : 1;
                        } else {
                            return (b[index[0]] < a[index[0]]) ? -1 : 1;
                        }
                    }
                });
                return items;
            }
        }
    }
</script>
