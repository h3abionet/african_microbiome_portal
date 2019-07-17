Vue.component('v-select', VueSelect.VueSelect);

let Alert = {
    template: '#alert',
    data: function() {
        return {
            errorMessage: state.errorMessage
        }
    },
    computed: {
        message: function () {
            return this.errorMessage
        }
    }
};

/* ---------------------------------------------------------*
 *      FILTER COMPONENTS                                   *
 * ---------------------------------------------------------*/
let SearchActions = {
    template: '#searchactions',
    data: function() {
        return {
            selectedValues: state.selectedValues,
            message: state.errorMessage
        }
    },
    methods: {
        filter (event) {
            event.preventDefault();
            let self = this;
            self.message = '';
            axios.post('/api/filter',
                self.selectedValues
            ).then(function (result) {
                self.$parent.updateRows(result.data.specimens);
                state.datasetRows = result.data.datasets;
            })
        }
    }
};

let SearchVue = {
    template: '#searchvue',
    props:['user', 'searchData', 'columns', 'selectedValues'],
    components: {
        'x-alert': Alert,
        'x-searchactions': SearchActions,
    },
    data() {
        return {
            selected: state.selected
        }
    },
    methods: {
        designColumn(arr) {
            this.$parent.updateColumns("Design", arr);
        },
        diseaseColumn(arr) {
            this.$parent.updateColumns("Disease", arr);
        },
        sexColumn(arr) {
            this.$parent.updateColumns("Sex", arr);
        },
        ethnicityColumn(arr) {
            this.$parent.updateColumns("Ethnicity", arr);
        },
        specTypeColumn(arr) {
            this.$parent.updateColumns("SpecType", arr);
        },
        countryColumn(arr) {
            this.$parent.updateColumns("Country", arr);
        },
        setSearchData(result) {
            this.$parent.setSearchData(result);
        },
        updateRows(result) {
            this.$parent.updateRows(result);
        }
    },
    created() {
        let self = this;
        axios.get('/api/data')
            .then(function (result) {
                self.setSearchData(result.data);
            })
    },
    /*mounted() {
        let self = this;
        $('select').change(function () {
            let val = $(this).val();
            if (val) {
                self.updateBmiOp(val);
            }
        })
    }*/
};

let ResultBioTable = {
    template: `
        <div class="container">
            <datatable 
                :name="name" 
                :title="title"
                :columns="columns"
                :rows="rows">
                
                <th slot="thead-tr">
                    Actions
                </th>
                <template slot="tbody-tr" slot-scope="props">
                    <td>
                        <a class="btn red darken-2 waves-effect waves-light compact-btn modal-trigger"
                                @click="(e) => openCartForm(props.row, e)" href="#request-modal">
                            <i class="material-icons white-text">shopping_cart</i>
                        </a>
                    </td>
                </template>
            </datatable>
        </div>
    `,
    props: ['columns', 'rows'],
    data: function () {
        return {
            name: "bio-table"
        }
    },
    computed: {
        title() {
            return "Found " + this.rows.length + " Studies"
        }
    },
    methods: {
        openCartForm: function(row, e) {
            this.$emit('row-selected', row);
        }
    }
};

let ResultDataTable = {
    template: `
        <div class="container">
            <datatable
                :name="name"
                :title="title"
                :columns="columns"
                :rows="rows">
            
                <th slot="thead-tr">
                    Actions
                </th>
                <template slot="tbody-tr" slot-scope="props">
                    <td>
                        <a class="btn red darken-2 waves-effect waves-light compact-btn"
                                @click="(e) => addDatasetToCart(props.row, e)">
                            <i class="material-icons white-text">shopping_cart</i>
                        </a>
                    </td>
                </template>
                
            </datatable>
        </div>
    `,
    data() {
        return {
            name: 'data-table',
            columns: state.dataColumns
        }
    },
    computed: {
        title() {
            return "Found " + this.rows.length + " Datasets"
        },
        rows() {
            return state.datasetRows;
        }
    },
    methods: {
        addDatasetToCart: function(row, e) {
            addDatasetToCart(row);
            row['added'] = true;
        }
    }
};

let Filter = {
    name: 'filter-app',
    template: '#filter',
    data: function () {
        return {
            searchData: state.searchData,
            selectedValues: state.selectedValues,
            columns: state.columns,
            rows: state.specimenRows,
            projectId: state.projectId
        }
    },
    components: {
        'x-searchvue': SearchVue,
        'x-biotable': ResultBioTable,
        'x-datatable': ResultDataTable
    },
    computed: {
        // Warning: user in data is empty. But computed get the user value.
        username() {
            return state.user.name;
        },
        cartId() {
            if (state.selectedCart !== null)
                return state.selectedCart.cartId
            return null;
        }
    },
    methods: {
        setSearchData(result) {
            this.searchData = result;
        },
        updateRows(result) {
            this.rows = result;
            state.specimenRows = this.rows;
        },
        updateColumns(column, arr) {
            switch (column) {
                case "Acronym":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.acronyms, "Acronym", "acronym");
                    else
                        removeSelectedValue(state.selectedValues.acronyms, "Acronym");
                    break;
                case "Design":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.designs, "Design", "design");
                    else
                        removeSelectedValue(state.selectedValues.designs, "Design");
                    break;
                case "Disease":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.diseases, "Disease", "disease");
                    else
                        removeSelectedValue(state.selectedValues.diseases, "Disease");
                    break;
                case "Sex":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.sex, "Sex", "sex");
                    else
                        removeSelectedValue(state.selectedValues.sex, "Sex");
                    break;
                case "Ethnicity":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.ethnicity, "Ethnicity", "ethnicity");
                    else
                        removeSelectedValue(state.selectedValues.ethnicity, "Ethnicity");
                    break;
                case "SpecType":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.specTypes, "SpecType", "specType");
                    else
                        removeSelectedValue(state.selectedValues.specTypes, "SpecType");
                    break;
                case "Country":
                    if (arr.length > 0)
                        addSelectedValue(state.selectedValues.countries, "Country", "country");
                    else
                        removeSelectedValue(state.selectedValues.countries, "Country");
                    break;
            }
        },
        setRowItem(row) {
            this.$parent.setRowItem(row);
        }
    }
};

let ModalBio = {
    name: "modal-test",
    template: `
    <div id="request-modal" class="modal modal-fixed-footer">
        <div class="modal-content">
            <div class="row">
                <div class="col m8">
                    <h5>Number of biospecimens to request</h5>
                </div>
                <div class="input-field col m3">
                    <input class="grey lighten-3" v-model="nbRequest" type="number" style="font-weight: bold"/>
                </div>
            </div>
            <div class="divider"></div>
            <div class="row">
                <div class="col m8">
                    <h6>Number of biospecimens available:</h6> 
                </div>
                <div class="col m3">
                    <h6>{{row.nbSamples}}</h6>
                </div>
                
            </div>
            <div class="row">
                <div class="col m8">
                    <h6>Number of biospecimens saved:</h6> 
                </div>
                <div class="col m3">
                    <h6 v-if="row.nbRequest">{{row.nbRequest}}</h6>
                    <h6 v-else>0</h6>
                </div>
                
            </div>
        </div>
        <div class="modal-footer">
            <a class="btn waves-effect waves-red modal-close h3africa white-text" href="#">Cancel</a>
            <a class="btn waves-effect waves-red modal-close h3africa white-text" @click="saveRequest" href="#">Save</a>
        </div>    
    </div>
    `,
    props: ['row'],
    data: function() {
        return {
            nbRequest: 0
        }
    },
    methods: {
        saveRequest: function () {
            this.row['nbRequest'] = this.nbRequest;
            this.nbRequest = 0;
            if (this.row.nbRequest > 0) {
                addIfNotExistsObjectArray(state.selectedRows, this.row);
            } else {
                removeObjectArray(state.selectedRows, this.row)

            }
        }
    }
};


/* ---------------------------------------------------------*
 *      MAIN COMPONENTS                                     *
 * ---------------------------------------------------------*/
let SideBar = {
    template: '#sidebar',
    props: ['user', 'nbRowSelected']
};

let routes = [
    {path: '/filter.html', component: Filter},
    {path: '/advance/carts', component: Carts},
    {path: '/advance/carts/cart', component: Cart},
    {path: '/advance/cart', component: YourCart},
    {path: '/advance/projects', component: Projects},
    {path: '/advance/projects/project', component: Project},
    {path: '/advance/projects/editProject', name: 'edit-project', component: EditProject, props: true}
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
        'x-modal': ModalBio,
        'x-cart-modal': CartModal
    },
    beforeCreate() {
        let self = this;
        axios.get('/api/user')
            .then(function (result) {
                self.currentUser(result.data);
            })
    },
    methods: {
        currentUser(user) {
            state.user = user;
        },
        setRowItem(row) {
            state.row = row;
        },
        setProjectId(projectId) {
            state.projectId = projectId;
        }
    }
});

