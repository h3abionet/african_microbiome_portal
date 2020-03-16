/* ---------------------------------------------------------*
 *      YOUR CART COMPONENTS                                *
 * ---------------------------------------------------------*/
let CartModal = {
    name: "modal-query",
    template: `
    <div id="query-modal" class="modal modal-fixed-footer">
        <div class="modal-content"> 
            <div class="row">
                <div class="col m8">
                    <h5>Query Values</h5>
                </div>
            </div>
            <div class="divider"></div>
            <div class="row" v-for="(value, key) in rowQuery">
                <div class="col m3">
                    <h5>{{ key }}</h5> 
                </div>
                <div class="col m8">
                    <h6>{{ value }}</h6>
                </div>
                
            </div>
        </div>
        <div class="modal-footer">
            <a class="btn waves-effect waves-red modal-close h3africa white-text" href="#">Close</a>
        </div>    
    </div>
    `,
    props: ['row'],
    computed: {
        rowQuery() {
            let query = {};
            let tempQuery = {};
            if (!_.isUndefined(this.row.query)) {
                tempQuery = this.row.query;
            } else {
                tempQuery = this.row;
            }
            let bmiOperator = null;
            let bmiValue = null;
            let ageOperator = null;
            let ageValue = null;
            _.each(this.row, function (val, key) {
                switch (key) {
                    case 'acronym':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Acronym'] = val;
                        }
                        break;
                    case 'design':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Design'] = val;
                        }
                        break;
                    case 'disease':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Disease'] = val;
                        }
                        break;
                    case 'sex':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Sex'] = val;
                        }
                        break;
                    case 'ethnicity':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Ethnicity'] = val;
                        }
                        break;
                    case 'country':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Country'] = val;
                        }
                        break;
                    case 'specimenType':
                        if (!_.isUndefined(val) && val !== null) {
                            query['Specimen Type'] = val;
                        }
                        break;
                    case 'smoking':
                        if (val === true) {
                            query['Smoking'] = 'Yes';
                        }
                        break;
                    case 'diet':
                        if (val === true) {
                            query['Diet'] = 'Yes';
                        }
                        break;
                    case 'hivStatus':
                        if (val === true) {
                            query['Hiv Status'] = 'Yes';
                        }
                        break;
                    case 'bloodPressure':
                        if (val === true) {
                            query['Blood Pressure'] = 'Yes';
                        }
                        break;
                    case 'alcoholUse':
                        if (val === true) {
                            query['Alcohol Use'] = 'Yes';
                        }
                        break;
                    case 'bmiOp':
                        if (!_.isUndefined(val) && val !== null) {
                            bmiOperator = val;
                        }
                        break;
                    case 'bmiVal':
                        if (!_.isUndefined(val) && val !== null) {
                            bmiValue = val;
                        }
                        break;
                    case 'ageOp':
                        if (!_.isUndefined(val) && val !== null) {
                            ageOperator = val;
                        }
                        break;
                    case 'ageVal':
                        if (!_.isUndefined(val) && val !== null) {
                            ageValue = val;
                        }
                        break;
                }
            });
            if (bmiOperator && bmiValue) {
                query['Bmi'] = bmiOperator + ' ' + bmiValue;
            }

            if (ageOperator && ageValue) {
                query['Age'] = ageOperator + ' ' + ageValue;
            }
            return query;
        }
    }
};


let DataSetTable = {
    template: `
        <div class="container">
            <datatable 
                :name="name" 
                :title="title"
                :columns="columns"
                :rows="rows">
                
                <th slot="thead-tr" v-if="status === 'Pending'">
                    Action
                </th>
                <template slot="tbody-tr" slot-scope="props">
                    <td v-if="status === 'Pending'">
                        <button class="btn red darken-2 waves-effect waves-light compact-btn"
                                @click="(e) => deleteRow(props.row, e)">
                            <i class="material-icons white-text">delete</i>
                        </button>
                    </td>
                </template>
            </datatable>
        </div>
    `,
    props : ['status'],
    data() {
        return {
            name: 'Dataset',
            title: 'Datasets Cart',
            columns: state.dataColumns
        }
    },
    computed: {
        rows() {
            return state.selectedDatasets;
        }
    },
    methods: {
        deleteRow(row, e) {
            removeElement(state.selectedDatasets, row);
            state.nbRowSelected -= 1;
        }
    }
};

let CartContent = {
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m10 l10">
                        <h5 class="breadcrumbs-title">Your Cart</h5>
                        <ol class="breadcrumbs">
                            <li><a href="index.html" style="color: #00bcd4;">{{ username }}</a></li>
                            <li><a href="index.html" style="color: #00bcd4;">{{ projectId }}</a></li>
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
            
            <div class="container" v-if="cartId === null">
                <div class="row" style="margin: auto 0.3rem auto 0.1rem">
                    <div id="card-alert" class="card pink lighten-5">

                        <div class="card-content pink-text darken-1">
                            <span class="card-title pink-text darken-1">No cart is selected</span>
                            <p>Select or create a project and a cart before using this search module.</p>
                        </div>
                        <div class="card-action pink lighten-4">
                            <router-link class="pink-text" to="/advance/carts">Ok</router-link>
                            <a th:href="@{/logout}" class="pink-text">Cancel</a>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="container" v-if="saveMessage !== null">
                <div id="card-alert" class="card green">
                      <div class="card-content white-text">
                        <p>SUCCESS : {{ saveMessage }}.</p>
                      </div>
                      <button type="button" class="close white-text" aria-label="Close" @click="closeMessage">
                        <span aria-hidden="true">×</span>
                      </button>
                </div>
            </div>
            
            <div class="container" v-if="cartId !== null">
                <datatable 
                    :name="name" 
                    :title="title"
                    :columns="columns"
                    :rows="selectedRows">
                    
                    <th slot="thead-tr">
                        Query
                    </th>
                    <th slot="thead-tr" v-if="status === 'Pending'">
                        Action
                    </th>
                    <template slot="tbody-tr" slot-scope="props">
                        <td>
                            <a class="btn red darken-2 waves-effect waves-light compact-btn modal-trigger"
                                    @click="(e) => showQuery(props.row, e)" href="#query-modal">
                                <i class="material-icons white-text">description</i>
                            </a>
                        </td>
                        <td v-if="status === 'Pending'">
                            <button class="btn red darken-2 waves-effect waves-light compact-btn"
                                    @click="(e) => deleteRow(props.row, e)">
                                <i class="material-icons white-text">delete</i>
                            </button>
                        </td>
                    </template>
                </datatable>
            </div>
            
            <x-data-table :status="status" v-if="cartId !== null"></x-data-table>
            
            <div class="container" v-if="cartId != null">
                <div class="row" id="work-collections">
                    <div class="col s12 m12 l12">
                        <ul id="projects-collection" class="collection">
                            <li class="collection-item avatar">
                                <i class="material-icons circle light-blue">shopping_cart</i>
                                <span class="collection-header">Cart</span>
                                <p>Information</p>
                            </li>
                            <li class="collection-item">
                                <div class="row">
                                    <div class="col s2">
                                        <p class="collections-title">CartId</p>
                                        <p class="collections-content">Provide a unique identifier to your cart</p>
                                    </div>
                                    <div class="col s6" v-if="status === 'Pending'">
                                        <input id="project-id" class="validate" type="text" v-model="newCartId"/>
                                    </div>
                                    <div class="col s6" v-else>
                                        <b>{{ cartId }}</b>
                                    </div>
                                </div>
                            </li>
                            <li class="collection-item">
                                <div class="row">
                                    <div class="col s12" v-if="status === 'Pending'">
                                            <input type="submit" value="Save" @click="saveCart">
                                            <input type="submit" value="Request" @click="requestCart">  
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
    `,
    components: {
        'x-data-table': DataSetTable
    },
    props: ['selectedRows', 'selectedDatasets'],
    data: function () {
        return {
            name: "Biospecimen",
            title: "Biospecimen Cart",
            username: state.user.name,
            projectId: state.projectId,
            columns: cartColumns,
            saveMessage: null,
            // newCartId: state.selectedCart.cartId
        }
    },
    computed: {
        dbId() {
            if (state.selectedCart !== null) {
                return state.selectedCart.id;
            }
            return null;
        },
        cartId() {
            if (state.selectedCart !== null) {
                return state.selectedCart.cartId;
            }
            return null;
        },
        status() {
            if (state.selectedCart !== null)
                return state.selectedCart.status;
            return null;
        },
        newCartId() {
            if (state.selectedCart !== null) {
                return state.selectedCart.cartId
            }
            return null;
        }
    },
    methods: {
        showQuery: function(row, e) {
            this.$emit('row-selected', row);
        },
        deleteRow: function (row, e) {
            this.$emit('delete-row', row);
        },
        saveCart() {
            let self = this;
            axios.post('/api/cart/update',
                {
                    dbId: [self.dbId],
                    newCartId: [self.newCartId],
                    bioRows: self.selectedRows,
                    dataRows: self.selectedDatasets
                }
            ).then(function (result) {
                self.saveMessage = result.data.return.message;
                state.selectedCart = result.data.return.cart;
            })
        },
        requestCart() {
            let self = this;
            axios.get(`/api/cart/request/${this.dbId}`)
                .then(function (result) {
                    self.saveMessage = result.data.return.message;
                    state.selectedCart = result.data.return.cart;
                })
        },
        closeMessage() {
            this.saveMessage = null
        }
    }
};

let YourCart = {
    name: 'your-cart',
    template: '#shopping-cart',
    data: function () {
        return {
            selectedRows: state.selectedRows,
            selectedDatasets: state.selectedDatasets
        }
    },
    components: {
        'x-cart-content': CartContent
    },
    methods: {
        setCartRow(row, e) {
            this.$parent.setRowItem(row);
        },
        deleteRow(row) {
            let self = this;
            axios.get(
                `/api/cart/remove/query/${row.id}`
            ).then(function (result) {
                //Todo: add an alert message
                self.$emit('card-deleted');
            });
            removeObjectArray(state.selectedRows, row);
        }
    }
};


/*------------------------------------------------------------*
 *         USER PROJECT CARTS                                 *
 *------------------------------------------------------------*/
let CartCard = {
    template: `
        <div class="card z-depth-0" v-if="card" v-bind:style="{opacity: opacity}">
            <div class="card-image h3africa waves-effect">
                <div class="card-title">{{ cartId }}</div>
                <div class="price">{{ queryLength }}</div>
                <div class="price-desc">Queries</div>
            </div>
            <div class="card-content">
                <ul class="collection">
                    <li class="collection-item">
                        <span>Status</span> 
                        <span class="task-cat grey darken-3 right" 
                            style="font-weight: bold;padding: 0 10px;font-size: 16px;">{{ cartStatus }}</span>
                    </li>
                </ul>
            </div>
            <div class="card-action center-align">                      
                <button class="waves-effect waves-light btn blue-grey">
                    <i class="material-icons">edit</i>
                </button>
                <button class="waves-effect waves-light btn blue-grey" @click="selectCart">
                    <i class="material-icons">check</i>
                </button>
                <button class="waves-effect waves-light btn blue-grey" @click="deleteCart">
                    <i class="material-icons">delete</i>
                </button>
            </div>
        </div>
    `,
    props: ['card'],
    computed: {
        dbId() {
            return this.card.cart.id;
        },
        cartId() {
            return this.card.cart.cartId;
        },
        status() {
            return this.card.cart.status;
        },
        queryLength() {
            return this.card.queries.length + this.card['data-queries'].length;
        },
        cartStatus() {
            return this.card.cart.status;
        },
        opacity() {
            if (state.selectedCart !== null) {
                if (this.card.cart.id === state.selectedCart.id) {
                    return 0.7;
                }
            }
            return 1;
        }
    },
    methods: {
        selectCart() {
            if (state.selectedCart === null || state.selectedCart.id !== this.card.cart.id) {
                state.selectedCart = this.card.cart;
                state.selectedRows = this.card.cart.queries;
                state.selectedDatasets = this.card['data-queries'];
                state.nbRowSelected = state.selectedRows.length + state.selectedDatasets.length;
                // convert id from integer to string (it's necessary for update cart)
                _.each(state.selectedRows, function (row) {
                    row['id'] = row['id'].toString();
                });
                _.each(state.selectedDatasets, function (row) {
                    row['id'] = row['id'].toString();
                });
            }
            else {
                state.selectedCart = null;
                state.selectedRows = null;
                state.nbRowSelected = 0;
            }
        },
        deleteCart() {
            let self = this;
            axios.get(`/api/cart/remove/${self.dbId}`)
                .then(function (result) {
                    self.successMessage = result.data.successMessage;
                    self.failureMessage = result.data.failureMessage;
                    if (self.successMessage !== null)
                        self.$emit('get-carts')
                });
        }
    }
};

let ProjectCarts = {
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Your Carts</h5>
                        <ol class="breadcrumbs">
                            <li><a href="/" style="color: #00bcd4;">Home</a></li>
                            <li><router-link to="/advance/projects" style="color: #00bcd4;">Projects</router-link></li>
                            <li class="active">Carts</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container" v-if="projectId === null">
                <div class="row" style="margin: auto 0.3rem auto 0.1rem">
                    <div id="card-alert" class="card pink lighten-5">

                        <div class="card-content pink-text darken-1">
                            <span class="card-title pink-text darken-1">No project is selected</span>
                            <p>Select or create a project to be able to see and create carts.</p>
                        </div>
                        <div class="card-action pink lighten-4">
                            <router-link class="pink-text" to="/advance/projects">Ok</router-link>
                            <a th:href="@{/logout}" class="pink-text">Cancel</a>
                        </div>

                    </div>
                </div>
            </div>
            
            <div class="container" v-if="successMessage !== null">
                <div id="card-alert" class="card green">
                      <div class="card-content white-text">
                        <p>SUCCESS : {{ successMessage }}.</p>
                      </div>
                      <button class="close white-text" aria-label="Close" @click="closeMessage">
                        <span aria-hidden="true">×</span>
                      </button>
                </div>
            </div>
            
            <div class="container" v-if="failureMessage !== null">
                <div id="card-alert" class="card orange">
                      <div class="card-content white-text">
                        <p>FAIL : {{ failureMessage }}.</p>
                      </div>
                      <button style="box-shadow: none" class="close white-text" aria-label="Close" @click="closeMessage">
                        <span aria-hidden="true">×</span>
                      </button>
                </div>
            </div>
            
            <div class="container">
                <p class="caption">
                    Create, edit, select and delete carts of project with id {{ projectId }}
                </p>
                <div class="divider"></div>
                <div class="row text-long-shadow text-info-filter" style="margin: 1rem 0.1rem">
                    <div class="col m8 l8">
                        <p v-if="cartId===null">
                            <i class="material-icons">warning</i>
                            <span class="project-selected">Click on 
                                <i class="material-icons">check</i> to select a cart.</span>
                        </p>
                        <p v-else>
                            <span class="project-selected">Cart
                                <span class="task-cat teal">
                                    {{ cartId }}</span> is selected.</span>
                        </p>
                    </div>
                    <div class="col m4 l4">
                        <router-link tag="button" to="/advance/carts/cart"
                                     class="btn waves-effect waves-light blue-grey right">
                            <i class="material-icons">add</i> Create Cart
                        </router-link>
                    </div>
                </div>
                    
                <div class="row">
                    <section id="plans" class="plans-container" v-for="i in loopLength">
                        <article class="col s12 m4 l4" v-for="j in 3">
                            <x-cart-card :card="cards[(i-1)*3+j-1]"
                                         @get-carts="getCarts"></x-cart-card>
                        </article>
                    </section>
                </div>
            </div>
        </section>
    `,
    data() {
        return {
            cards: [],
            projectId: state.projectId,
            username: state.user.name,
            successMessage: null,
            failureMessage: null
        }
    },
    computed: {
        cartId() {
            if (state.selectedCart !== null)
                return state.selectedCart.cartId;
            return null;
        },
        loopLength() {
            return Math.floor((this.cards.length -1) / 3 + 1);
        }
    },
    components: {
        'x-cart-card': CartCard
    },
    methods: {
        closeMessage() {
            this.successMessage = null;
            this.failureMessage = null;
        },
        setCarts(cards) {
            this.cards = cards;
            _.each(this.cards, function (card) {
                card.cart.queries = card.queries;
            })
        },
        getCarts() {
            let self = this;
            if (self.projectId !== null) {
                axios.get(`/api/carts/${self.projectId}`)
                    .then(function (result) {
                        self.setCarts(result.data['cart-queries']);
                    })
            }
        }
    },
    created() {
        this.getCarts();
    }
};

let Carts = {
    name: 'carts',
    template: '#project-carts',
    data() {
        return {
            projectId: state.projectId,
        }
    },
    components: {
        'x-carts': ProjectCarts
    }
};

/*------------------------------------------------------*
 *            Create Cart                               *
 *------------------------------------------------------*/
let Cart = {
    name:'cart-create',
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Add New Cart</h5>
                        <ol class="breadcrumbs">
                            <li><a href="index.html" style="color: #00bcd4;">{{ username }}</a></li>
                            <li><a href="index.html" style="color: #00bcd4;">{{ projectId }}</a></li>
                            <li class="active">{{ cartId }}</li>
                        </ol>
                    </div>
                </div>
            </div>
            
            <div class="container">
                <p class="caption">
                    The form below, create and initiate a new empty cart.
                </p>
                <div class="divider"></div>
                <form id="project-form" class="col m10" @submit="checkForm" method="post">
                    <div class="row">
                        <p v-if="errors.length">
                            <b>Please correct the following error(s):</b>
                            <ul>
                                <li v-for="error in errors" style="color: #ff3d00">{{ error }}</li>
                            </ul>
                            <div v-if="errors.length" class="divider"></div>
                        </p>
                    </div>
                    
                    <div class="row margin">
                        <div class="input-field col s9">
                            <p>1.
                                <span style="font-weight: bold;">Provide a unique cart identifier</span>
                            </p>
                            <input id="project-id" class="validate" type="text" v-model="cartId"/>
                        </div>
                    </div>
                    <div class="row" style="padding-top: 5px;">
                        <p>
                            <input type="submit" value="Submit">  
                        </p>
                    </div>
                </form>
            </div>
        </section>
    `,
    data() {
        return {
            username: state.user.name,
            projectId: state.projectId,
            cartId: '',
            errors:[]
        }
    },
    methods: {
        checkForm(e) {
            e.preventDefault();
            this.erros = [];
            if (!this.cartId) {
                this.errors.push('Cart Id required.');
            }
            if (!this.projectId) {
                this.errors.push('Select or create a project before creating a cart.')
            }
            if (this.erros.length === 0) {
                var self = this;
                axios.post('/api/cart/create',
                    {
                        cartId: self.cartId,
                        projectId: self.projectId
                    }
                ).then(function (result) {
                    self.$router.push("/advance/carts");
                })
            }
        }
    }
};
