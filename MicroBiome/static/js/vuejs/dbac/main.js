let SideBar = {
    template: '#sidebar',
    props: ['user']
};

let RequestedCarts = {
    name: 'requestedCarts',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Requested Carts</h5>
                        <ol class="breadcrumbs">
                            <li><a href="/" style="color: #00bcd4;">Home</a></li>
                            <li class="active">Requests</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" style="background: #ececec;height: 700px;overflow: auto;">
                <div class="row" style="margin: auto 0.3rem auto 0.1rem">
                    <p class="request-header">
                        <i class="material-icons inline-icon">view_module</i> Carts</p>
                     
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Cart Id</th>
                            <th>Project Id</th>
                            <th>User</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="cart in requestedCarts">
                            <td>
                                <a href="#" @click="showCart(cart)">
                                    <b class="blue-text">{{ cart.cartId }}</b>
                                </a>
                            </td>
                            <td>
                                <a href="#" class="blue-text" @click="showProject(cart)">
                                    {{ cart.projectId }}
                                </a>
                            </td>
                            <td>
                                <a href="#" class="blue-text" @click="showUser(cart)">
                                    {{ cart.username }}
                                    </a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    `,
    computed: {
        // Warning: user in data is empty. But computed get the user value.
        username() {
            return state.user.name;
        },
        requestedCarts() {
            return state.requestedCarts
        }
    },
    methods: {
        showCart(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/cart');
        },
        showProject(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/project')
        },
        showUser(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/user')
        }
    },
    beforeCreate() {
        let self = this;
        axios.get('/api/requested/carts')
            .then(function (result) {
                state.requestedCarts = result.data.requestedCarts;
            });
        state.statusCarts = 'Requested';
    }
};

let RejectedCarts = {
    name: 'rejectedCarts',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Rejected Carts</h5>
                        <ol class="breadcrumbs">
                            <li><a href="index.html" style="color: #00bcd4;">{{ username }}</a></li>
                            <li class="active">Requests</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" style="background: #ececec;height: 700px;overflow: auto;">
                <div class="row" style="margin: auto 0.3rem auto 0.1rem">
                    <p class="request-header">
                        <i class="material-icons inline-icon">view_module</i> Carts</p>
                     
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Cart Id</th>
                            <th>Project Id</th>
                            <th>User</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="cart in rejectedCarts">
                            <td>
                                <a href="#" @click="showCart(cart)">
                                    <b class="blue-text">{{ cart.cartId }}</b>
                                </a>
                            </td>
                            <td>
                                <a href="#" class="blue-text" @click="showProject(cart)">
                                    {{ cart.projectId }}
                                </a>
                            </td>
                            <td>
                                <a href="#" class="blue-text" @click="showUser(cart)">
                                    {{ cart.username }}
                                    </a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    `,
    computed: {
        // Warning: user in data is empty. But computed get the user value.
        username() {
            return state.user.name;
        },
        rejectedCarts() {
            return state.rejectedCarts
        }
    },
    methods: {
        showCart(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/cart');
        },
        showProject(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/project')
        },
        showUser(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/user')
        }
    },
    beforeCreate() {
        let self = this;
        axios.get('/api/rejected/carts')
            .then(function (result) {
                state.rejectedCarts = result.data.rejectedCarts;
            });
        state.statusCarts = 'Rejected';
    }
};

let ApprovedCarts = {
    name: 'approvedCarts',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Approved Carts</h5>
                        <ol class="breadcrumbs">
                            <li><a href="index.html" style="color: #00bcd4;">{{ username }}</a></li>
                            <li class="active">Requests</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" style="background: #ececec;height: 700px;overflow: auto;">
                <div class="row" style="margin: auto 0.3rem auto 0.1rem">
                    <p class="request-header">
                        <i class="material-icons inline-icon">view_module</i> Carts</p>
                     
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Cart Id</th>
                            <th>Project Id</th>
                            <th>User</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="cart in approvedCarts">
                            <td>
                                <a href="#" @click="showCart(cart)">
                                    <b class="blue-text">{{ cart.cartId }}</b>
                                </a>
                            </td>
                            <td>
                                <a href="#" class="blue-text" @click="showProject(cart)">
                                    {{ cart.projectId }}
                                </a>
                            </td>
                            <td>
                                <a href="#" class="blue-text" @click="showUser(cart)">
                                    {{ cart.username }}
                                    </a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    `,
    computed: {
        // Warning: user in data is empty. But computed get the user value.
        username() {
            return state.user.name;
        },
        approvedCarts() {
            return state.approvedCarts
        }
    },
    methods: {
        showCart(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/cart');
        },
        showProject(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/project')
        },
        showUser(cart) {
            state.selectedCart = cart;
            this.$router.push('/dbac/status/user')
        }
    },
    beforeCreate() {
        let self = this;
        axios.get('/api/approved/carts')
            .then(function (result) {
                state.approvedCarts = result.data.approvedCarts;
            });
        state.statusCarts = 'Approved';
    }
};

let CartModal = {
    name: "modal-query",
    template: `
    <div id="query-modal" class="modal modal-fixed-footer">
        <div class="modal-content"> 
            <div class="row">
                <div class="col m8">
                    <h5>Query values</h5>
                </div>
            </div>
            <div class="divider"></div>
            <div class="row" v-for="(value, key) in rowQuery">
                <div class="col m5">
                    <h5>{{ key }}</h5> 
                </div>
                <div class="col m7">
                    <h6>{{ value }}</h6>
                </div>
                
            </div>
        </div>
        <div class="modal-footer">
            <a class="btn waves-effect waves-red modal-close h3africa white-text" href="#">Close</a>
        </div>    
    </div>
    `,
    props: ['query'],
    computed: {
        rowQuery() {
            let modifiedQuery = {};
            _.each(this.query, function (val, key) {
                switch (key) {
                    case 'acronym':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Acronym'] = val;
                        }
                        break;
                    case 'design':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Design'] = val;
                        }
                        break;
                    case 'disease':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Disease'] = val;
                        }
                        break;
                    case 'sex':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Sex'] = val;
                        }
                        break;
                    case 'ethnicity':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Ethnicity'] = val;
                        }
                        break;
                    case 'country':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Country'] = val;
                        }
                        break;
                    case 'specimenType':
                        if (!_.isUndefined(val) && val !== null) {
                            modifiedQuery['Specimen Type'] = val;
                        }
                        break;
                    case 'smoking':
                        if (val === true) {
                            modifiedQuery['Smoking'] = 'Yes';
                        }
                        break;
                    case 'diet':
                        if (val === true) {
                            modifiedQuery['Diet'] = 'Yes';
                        }
                        break;
                    case 'hivStatus':
                        if (val === true) {
                            modifiedQuery['HIV Status'] = 'Yes';
                        }
                        break;
                    case 'bloodPressure':
                        if (val === true) {
                            modifiedQuery['Blood Pressure'] = 'Yes';
                        }
                        break;
                    case 'alcoholUse':
                        if (val === true) {
                            modifiedQuery['Alcohol Use'] = 'Yes';
                        }
                        break;
                    case 'bmiOp':
                        if (this.query['bmiVal']) {
                            modifiedQuery['Bmi'] = val + ' ' + this.query['bmiVal'];
                        }
                        break;
                    case 'ageOp':
                        if (this.query['ageVal']) {
                            modifiedQuery['Age'] = val + ' ' + this.query['ageVal'];
                        }
                        break;
                }
            });
            return modifiedQuery;
        }
    }
};

let SelectedCart = {
    name: 'requestedCart',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m10 l10">
                        <h5 class="breadcrumbs-title">Cart 
                            <span class="task-cat white-text h3africa"><b>{{ cartId }}</b></span></h5>
                        <ol class="breadcrumbs">
                            <li v-if="status==='Requested'">
                                <router-link to="/dbac.html" style="color: #00bcd4;">{{ status }} Carts</router-link>
                            </li>
                            <li v-if="status==='Approved'">
                                <router-link to="/dbac/approved" style="color: #00bcd4;">{{ status }} Carts</router-link>
                            </li>
                            <li v-if="status==='Rejected'">
                                <router-link to="/dbac/rejected" style="color: #00bcd4;">{{ status }} Carts</router-link>
                            </li>
                            <li class="active">{{ cartId }}</li>
                        </ol>
                    </div>
                    <div class="col s12 m2 l2" style="margin-top: 1rem">
                        <div class="chip teal white-text right" style="max-width:70%;">
                                {{ status }}
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="container" v-if="statusMessage !== null">
                <div id="card-alert" class="card green">
                      <div class="card-content white-text">
                        <p>SUCCESS : {{ statusMessage }}</p>
                      </div>
                      <button type="button" class="close white-text" aria-label="Close" @click="closeMessage">
                        <span aria-hidden="true">×</span>
                      </button>
                </div>
            </div>
            
            <div class="container" style="background-color:#ececec;height:auto;">
                <div class="row" style="margin: auto 0.3rem auto 0.1rem;" v-if="queries.length > 0">
                    <p class="request-header" style="padding-top: 20px">
                        <i class="material-icons inline-icon">colorize</i> Biospecimen Queries</p>
                     
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Query ID</th>
                            <th>Acronym</th>
                            <!--<th>Design</th>-->
                            <!--<th>Disease</th>-->
                            <th>Nb Request</th>
                            <th>Query</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="query in queries">
                            <td>
                                <a href="#" @click="queryBiospecimens(query)">
                                    <b class="blue-text">{{ query.id }}</b>
                                </a>
                            </td>
                            <td>{{ query.acronym }}</td>
                            <!--<td>{{ query.design }}</td>-->
                            <!--<td>{{ query.disease}}</td>-->
                            <td><b class="task-cat red darken-2 white-text" style="font-size: 14px;padding: 0.2rem 0.6rem">
                                {{ query.nbRequest }}</b></td>
                            <td>
                                <a class="btn red darken-2 waves-effect waves-light compact-btn modal-trigger"
                                    @click="(e) => showQuery(query, e)" href="#query-modal">
                                    <i class="material-icons">description</i>
                                </a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                
                <div class="row" style="height: 15px;background-color: white"></div>
                
                <div class="row" style="margin: auto 0.3rem auto 0.1rem;" v-if="dataQueries.length > 0">
                    <p class="request-header" style="padding-top: 20px">
                        <i class="material-icons inline-icon">view_module</i> Dataset Queries</p>
                     
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Acronym</th>
                            <th>EGA Access</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="query in dataQueries">
                            <td>
                                <a href="#" @click="showQuery(query)">
                                    <b class="blue-text">{{ query.acronym }}</b>
                                </a>
                            </td>
                            <td>{{ query.egaAccess }}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                
                <div class="divider"></div>
                <div class="row" v-if="status === 'Requested'">
                    <div class="col s12" style="margin: 0.75rem auto;">
                            <input type="submit" value="Approve" @click="approveCart">
                            <input type="submit" value="Reject" @click="rejectCart">  
                    </div>
                </div>
                <div class="row" v-else>
                    <div class="col s12" style="margin: 0.75rem auto;">
                        <input type="submit" value="Reinstate" @click="reinstateCart">
                    </div>
                </div>
            </div>
        </section>
    `,
    data() {
        return {
            username: state.selectedCart.username,
            projectId: state.selectedCart.projectId,
            cartId: state.selectedCart.cartId,
            status: state.selectedCart.status,
            queries: state.selectedCart.queries,
            dataQueries: state.selectedCart.dataQueries,
            statusMessage: null
        }
    },
    methods: {
        approveCart() {
            let self = this;
            axios.post('/api/dbac/cart/status',
                {
                    cartId: self.cartId,
                    projectId: self.projectId,
                    username: self.username,
                    status: 'Approved'
                })
                .then(function (result) {
                    self.statusMessage = result.data.message;
                    self.status = 'Approved';
                })
        },
        rejectCart() {
            let self = this;
            axios.post('/api/dbac/cart/status',
                {
                    cartId: self.cartId,
                    projectId: self.projectId,
                    username: self.username,
                    status: 'Rejected'
                })
                .then(function (result) {
                    self.statusMessage = result.data.message;
                    self.status = 'Rejected';
                })
        },
        reinstateCart() {
            let self = this;
            axios.post('/api/dbac/cart/status',
                {
                    cartId: self.cartId,
                    projectId: self.projectId,
                    username: self.username,
                    status: 'Requested'
                })
                .then(function (result) {
                    self.statusMessage = result.data.message;
                    self.status = 'Requested'
                })
        },
        queryBiospecimens(query) {
            state.selectedQuery = query;
            axios.get(`/api/dbac/query/biospecimens/${query.id}`)
                .then(function (result) {
                    if (result.data.specimens.length > 0) {
                        state.querySpecimens = result.data.specimens;
                    }
                });
            this.$router.push('/dbac/query/specimens')
        },
        showQuery(query, e) {
            this.$parent.showQuery(query);
        },
        closeMessage() {
            this.statusMessage = null
        }
    }
};

let SpecimenQueries = {
    name: 'specimenQueries',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Cart 
                            <span class="task-cat white-text h3africa"><b>{{ cartId }}</b></span></h5>
                        <ol class="breadcrumbs">
                            <li>
                                <router-link to="/dbac/status/user" style="color: #00bcd4;">{{ username }}</router-link>
                            </li>
                            <li>
                                <router-link to="/dbac/status/cart" style="color: #00bcd4;">{{ cartId }}</router-link>
                            </li>
                            <li class="active">
                                <router-link to="/dbac/query/specimens" style="color: #00bcd4;">{{ queryId }}</router-link>
                            </li>
                            <li class="active">Queries</li>
                        </ol>
                    </div>
                </div>
            </div>
            <div class="container" style="background: #ececec;height:auto;">
                <div class="row" style="margin: 1rem 0.3rem auto 0.1rem">
                    <p class="request-header">
                        <i class="material-icons inline-icon">view_module</i> Queries</p>
                     
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Biospecimen ID</th>
                            <th>Query ID</th>
                            <th>Total Nb Requested</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="query in queries">
                            <td>{{ query.specimenId }}</td>
                            <td>{{ query.queryId }}</td>
                            <td><span class="task-cat teal" style="padding: 0.2rem 0.6rem;font-size: 14px;">
                                <b>{{ query.nbRequest }}</b></span></td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    `,
    data() {
        return {
            username: state.selectedCart.username,
            cartId: state.selectedCart.cartId,
        }
    },
    computed: {
        queryId() {
            return state.selectedQuery.id;
        },
        queries() {
            return state.specimenQueries;
        }
    }
};

let QuerySpecimens = {
    name: 'querySpecimens',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Cart 
                            <span class="task-cat white-text h3africa"><b>{{ cartId }}</b></span></h5>
                        <ol class="breadcrumbs">
                            <li v-if="status==='Requested'">
                                <router-link to="/dbac.html" style="color: #00bcd4;">{{ status }} Carts</router-link>
                            </li>
                            <li v-if="status==='Approved'">
                                <router-link to="/dbac/approved" style="color: #00bcd4;">{{ status }} Carts</router-link>
                            </li>
                            <li v-if="status==='Rejected'">
                                <router-link to="/dbac/rejected" style="color: #00bcd4;">{{ status }} Carts</router-link>
                            </li>
                            <li>
                                <router-link to="/dbac/status/cart" style="color: #00bcd4;">{{ cartId }}</router-link>
                            </li>
                            <li class="active">{{ queryId }}</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" style="background: #ececec;height:auto;">
                <div class="row" style="padding-top: 1rem">
                    <div class="col s3 m3 l3">
                        <span class="request-header">
                            <i class="material-icons inline-icon">colorize</i> Biospecimens</span>
                    </div>
                    <div class="col s3 m3 l3">
                        <div class="right" style="margin-right: 2rem">
                            <span class="task-cat orange task-cat-emp"><b>Total</b></span>
                            <span class="task-cat teal task-cat-emp">{{ nbTotalSpec }}</span>
                        </div>
                    </div>
                    <div class="col s3 m3 l3">
                        <div class="right" style="margin-right: 2rem">
                            <span class="task-cat orange task-cat-emp"><b>Assigned</b></span>
                            <span class="task-cat teal task-cat-emp">{{ nbLinkedSpec }}</span>
                        </div>
                    </div>
                    <div class="col s3 m3 l3">
                        <div class="right" style="margin-right: 2rem">
                            <span class="task-cat orange task-cat-emp"><b>Requested</b></span>
                            <span class="task-cat teal task-cat-emp">{{ nbRequest }}</span>
                        </div>
                    </div>
                </div> 
                <div class="row" style="margin: 1rem 0.2rem">    
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th>Biospecimen ID</th>
                            <th>Nb Aliquots</th>
                            <th>Biobank</th>
                            <th>Action</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="biospecimen in biospecimens" :style="backgroundColor(biospecimen)">
                            <td>
                                <a href="#" @click="findSpecimenQueries(biospecimen)">
                                    <b style="color: #00bcd4;">{{ biospecimen.id }}</b>
                                </a>
                            <td>{{ biospecimen.aliquots}}</td>
                            <td>{{ biospecimen.biobank}}</td>
                            <td>
                                <a class="btn red darken-2 waves-effect waves-light compact-btn" 
                                   @click="linkSpecimenQuery(biospecimen)" v-if="biospecimen.linked === false">
                                   <i class="material-icons">done</i> 
                                </a>
                                <a class="btn red darken-2 waves-effect waves-light compact-btn" 
                                   @click="unlinkSpecimenQuery(biospecimen)" v-if="biospecimen.linked === true">
                                   <i class="material-icons">close</i> 
                                </a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>
    `,
    data() {
        return {
            username: state.selectedCart.username,
            cartId: state.selectedCart.cartId,
            status: state.selectedCart.status,
            message: null,
            error: null
        }
    },
    computed: {
        biospecimens() {
            return state.querySpecimens;
        },
        queryId() {
            return state.selectedQuery.id;
        },
        nbRequest() {
            return state.selectedQuery.nbRequest;
        },
        nbLinkedSpec() {
            let temp = state.querySpecimens.filter((s) => s.linked === true);
            return temp.length;
        },
        nbTotalSpec() {
            return state.querySpecimens.length;
        }
    },
    methods: {
        linkSpecimenQuery(row) {
            row['queryId'] = this.queryId;
            row['nbRequest'] = this.nbRequest;
            let self = this;
            axios.post('/api/dbac/linkSpecimenQuery',
                 row
            ).then(function (result) {
                self.message = result.data.message;
                self.error = result.data.error;
                if (self.error == null) {
                    let item = state.querySpecimens.find(item => item.id === row.id);
                    item.linked = true;
                }
            })
        },
        unlinkSpecimenQuery(row) {
            row['queryId'] = this.queryId;
            row['nbRequest'] = this.nbRequest;
            let self = this;
            axios.post('/api/dbac/unlinkSpecimenQuery',
                row
            ).then(function (result) {
                self.message = result.data.message;
                self.error = result.data.error;
                if (self.error == null) {
                    let item = state.querySpecimens.find(item => item.id === row.id);
                    item.linked = false;
                }
            })
        },
        findSpecimenQueries(row) {
            let self = this;
            axios.get(`/api/dbac/specimen/queries/${row.id}/${self.queryId}`)
                .then(function (result) {
                    state.specimenQueries = result.data.queries;
                    self.$router.push('/dbac/specimen/queries');
                });
        },
        backgroundColor(row) {
            if (row.linked === true) {
                return {background: '#fcfa92'}
            }
        }
    }
};

let ProjectCart = {
    name:'projectCart',
    template: `
        <section id="content" style="margin-left: 240px;">
        
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Cart 
                            <span class="task-cat white-text h3africa"><b>{{ cartId }}</b></span></h5>
                        <ol class="breadcrumbs">
                            <li><router-link to="/dbac/status/cart" style="color: #00bcd4;">{{ cartId }}</router-link></li>
                            <li class="active">{{ projectId }}</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" style="border: 1px solid greenyellow;">
                <div class="row col s12 m9 l9" style="margin: 1rem">
                    <div>
                        <p>1.
                            <span style="font-weight: bold;">Title of project (less than 30 words)</span>
                        </p>
                        <p class="blue-text text-darken-4">{{ project.projectTitle }}</p>
                    </div>
                    
                    <div>
                        <p>2.
                            <span style="font-weight: bold;">Research Question (less than 1000 words)</span>
                            Please provide a <span style="font-weight: bold;">clear</span> description of the project and
                            its specific aims. Include: a. outline of the study design; b. which disease and/or control genotypes
                            you require; c. timeline; d. key references
                        </p>
                        <p class="blue-text text-darken-4">{{ project.researchQuestion }}</p>
                    </div>
                    <div>
                        <p>2.1
                            <span style="font-weight: bold;">For Biospecimen requests</span>
                            Please provide a <span style="font-weight: bold;">clear</span> description of a. the methodologies
                            to be used on the biospecimens; b. specific details of what you plan to do with the biospecimens.
                        </p>
                        <p class="blue-text text-darken-4">{{ project.researchBioRequests }}</p>
                    </div>
                    <div>
                        <p>2.2
                            <span style="font-weight: bold;">For Data requests</span>
                            Please provide a <span style="font-weight: bold;">clear</span> description of a. the methodologies
                            to be used on the data; b. specific details of what you plan to do with the data.
                        </p>
                        <p class="blue-text text-darken-4">{{ project.researchDataRequests }}</p>
                    </div>
                    <div>
                        <p>3.
                            <span style="font-weight: bold;">Details of data/biospecimens requested</span></p>
                        <p>3.1
                            <span style="font-weight: bold;"> For Biospecimen requests</span> The project biospecimen applied for
                        </p>
                        <p class="blue-text text-darken-4">{{ project.detailBioRequests}}</p>
                        <p>3.2
                            <span style="font-weight: bold;"> For Data requests</span> The project data applied for
                        </p>
                        <p class="blue-text text-darken-4">{{ project.detailDataRequests }}</p>
                    </div>
                    <div>
                        <p>3.3
                            <span style="font-weight: bold;">Please tick the box below, if you request the associated phenotype
                                data</span>
                        </p>
                        <p class="blue-text text-darken-4">{{ phenoData }}</p>
                    </div>
                    <div>
                        <p>4.
                            <span style="font-weight: bold;">Research ethics</span>
                            Do you forsee any ethical issues, including potential harms to data subjects such as potential
                            stigmatisation of ethic groups, arising as a result of your research? If so, how do you plan to
                            address such issues?
                        </p>
                        <p class="blue-text text-darken-4">{{ project.researchEthics }}</p>
                    </div>
                    <div>
                        <p>5.
                            <span style="font-weight: bold;">Benefits to Africa</span>
                            The goal of the H3Africa is to improve the health of African populations, and to contribute to
                            the development of expertise and research capacity among African scientists. How do you see your
                            proposed use of the data and biospecimens contributing to this?
                        </p>
                        <p class="blue-text text-darken-4">{{ project.benifitsAfrica }}</p>
                    </div>
                    <div>
                        <p>5.1
                            <span style="font-weight: bold;">Please list your African collaborators</span>
                            (this is required for biospecimens for the first 3 years after submission -see policy
                            document on the website)
                        </p>
                        <p class="blue-text text-darken-4">{{ project.africanCollaborators }}</p>
                    </div>
                    <div>
                        <p>6.
                            <span style="font-weight: bold;">Resources, Feasibility &amp; Expertise (less than 1000)</span>
                            Please describe fully your experience and expertise and that of your collaborators, wether there
                            is secured funding for your proposed use of the data and/or biospecimens, and how this will be
                            applied to the proposed study. A publication list (max 10) <span style="font-width:bold;">Must</span>
                            be provided for the applicant and co-applicants. The committee needs assurance of competence in hanging
                            datasets of this size and nature or such samples.
                        </p>
                        <p class="blue-text text-darken-4">{{ project.feasibility }}</p>
                    </div>
                    <div>
                        <p>7.
                            <span style="font-weight: bold;">Consent and Approvals</span>
                            Please confirm that you have obtained all approvals required for this project by the rules and
                            regulations of your jurisdiction, including your institution's institutional rules and any
                            relevant national rules, by ticking the following box: (you may be requested to provide a copy
                            of the consent form, particularly for biospecimen requests)
                        </p>
                        <p class="blue-text text-darken-4">{{ project.consentApprovals }}</p>
                    </div>
                    <div>
                        <p>
                            <span style="font-weight: bold;">For Biospecimen requests<br/>
                            I have read and agree to abide by the terms and conditions outlined in the H3Africa Biospecimen
                            Sharing Policy and will sign the Material Transfer Agreement negotiated with the host biorepository
                            </span>
                        </p>
                        <p class="blue-text text-darken-4">{{ project.consentBioRequests }}</p>
                    </div>
                    <div>
                        <p>
                            <span style="font-weight: bold;">For Data requests<br/>
                            I have read and agree to abide by the terms and conditions outlined in the Data Access
                            Agreement and the Publication Policy?</span>
                        </p>
                        <p class="blue-text text-darken-4">{{ project.consentDataRequests }}</p>
                    </div>
                </div>
            </div>
        </section>
    `,
    data() {
        return {
            id: state.selectedCart.id,
            cartId: state.selectedCart.cartId,
            username: state.selectedCart.username,
            projectId: state.selectedCart.projectId,
            project: {}
        }
    },
    computed: {
        phenoData() {
            return (this.project.phenoDataRequested ? "Yes" : "No");
        }
    },
    created() {
        let self = this;
        axios.get(`/api/dbac/cart/project/${self.id}`)
            .then(function (result) {
                self.project = result.data.project;
            })
    }
};

let UserCart = {
    name: 'userCart',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Cart
                            <span class="task-cat white-text h3africa"><b>{{ cartId }}</b></span></h5>
                        <ol class="breadcrumbs">
                            <li><router-link to="/dbac/status/cart" style="color: #00bcd4;">{{ cartId }}</router-link></li>
                            <li class="active">USER</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" style="border: 1px solid greenyellow;">
                <div class="row col s12 m9 l9" style="margin: 1rem">
                    <div class="row">
                        <div class="col m4">
                            <span style="font-weight: bold;">First Name</span>
                        </div>
                        <div class="col m8">
                            <p class="blue-text text-darken-4">{{ user.firstName}}</p>
                        </div>
                    </div>
                    <div class="divider"></div>
                    <div class="row">
                        <div class="col m4">
                            <span style="font-weight: bold;">Last Name</span>
                        </div>
                        <div class="col m8">
                            <p class="blue-text text-darken-4">{{ user.lastName}}</p>
                        </div>
                    </div>
                    <div class="divider"></div>
                    <div class="row">
                        <div class="col m4">
                            <span style="font-weight: bold;">Email</span>
                        </div>
                        <div class="col m8">
                            <p class="blue-text text-darken-4">{{ user.email}}</p>
                        </div>
                    </div>
                    <div class="divider"></div>
                    <div class="row">
                        <div class="col m4">
                            <span style="font-weight: bold;">Institution Name</span>
                        </div>
                        <div class="col m8">
                            <p class="blue-text text-darken-4">{{ user.institution}}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    `,
    data() {
        return {
            user: {},
            id: state.selectedCart.id,
            cartId: state.selectedCart.cartId,
            username: state.selectedCart.username,
        }
    },
    created() {
        let self = this;
        axios.get(`/api/dbac/cart/user/${self.id}`)
            .then(function (result) {
                console.log(result.data)
                self.user = result.data.user;
            })
    }
};

let routes = [
    {path: '/dbac.html', component: RequestedCarts},
    {path: '/dbac/approved', component: ApprovedCarts},
    {path: '/dbac/rejected', component: RejectedCarts},
    {path: '/dbac/status/cart', component: SelectedCart},
    {path: '/dbac/status/project', component: ProjectCart},
    {path: '/dbac/status/user', component: UserCart},
    {path: '/dbac/query/specimens', component: QuerySpecimens},
    {path: '/dbac/specimen/queries', component: SpecimenQueries},
];

let router = new VueRouter({
    mode: 'history',
    routes: routes
});

new Vue({
    el: '#root',
    data: state,
    router: router,
    components: {
        'x-sidebar': SideBar,
        'x-modal': CartModal
    },
    beforeCreate() {
        let self = this;
        axios.get('/api/user')
            .then(function (result) {
                self.currentUser(result.data);
            })
    },
    methods :{
        currentUser(user) {
            state.user = user;
        },
        showQuery(query) {
            state.query = query;
        },
    }
});