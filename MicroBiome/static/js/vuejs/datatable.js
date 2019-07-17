Vue.component('datatable', {
    template: `
    
    <div class="card material-table">
		<div class="table-header" style="background-color: #ECECEC">
			<span class="table-title">{{title}}</span>
			<div class="actions">
				<a v-for="button in customButtons" href="javascript:undefined"
				   class="waves-effect btn-flat nopadding"
				   v-if="button.hide ? !button.hide : true"
				   @click="button.onclick">
					<i class="material-icons">{{button.icon}}</i>
				</a>
				<a href="javascript:undefined"
					class="waves-effect btn-flat nopadding"
					v-if="this.printable"
					@click="print">
					<i class="material-icons">print</i>
				</a>
				<a href="javascript:undefined"
					class="waves-effect btn-flat nopadding"
					v-if="this.exportable"
					@click="exportExcel">
					<i class="material-icons">description</i>
				</a>
				<a href="javascript:undefined"
					class="waves-effect btn-flat nopadding"
					v-if="this.searchable"
					@click="search">
					<i class="material-icons">search</i>
				</a>
			</div>
		</div>
		<div v-if="this.searching">
			<div id="search-input-container">
				<label>
					<input type="search" id="search-input" class="form-control" :placeholder="lang['search_data']"
						:value="searchInput"
						@input="(e) => {this.searchInput = e.target.value}">
				</label>
			</div>
		</div>
		<table ref="table">
			<thead>
				<tr>
					<th v-for="(column, index) in columns"
						@click="sort(index)"
						:class="(sortable ? 'sorting ' : '')
							+ (sortColumn === index ?
								(sortType === 'desc' ? 'sorting-desc' : 'sorting-asc')
								: '')
							+ (column.numeric ? ' numeric' : '')"
						:style="{width: column.width ? column.width : 'auto'}">
						{{column.label}}
					</th>
					<slot name="thead-tr"></slot>
				</tr>
			</thead>

			<tbody>
				<tr v-for="(row, index) in paginated" :class="{ clickable : clickable }" @click="click(row)">
					<td v-for="column in columns" :class=" { numeric : column.numeric } ">
						<div v-if="!column.html"> {{ collect(row, column.field) }} </div>
						<div v-if="column.html" v-html="collect(row, column.field)"></div>						
					</td>
					<slot name="tbody-tr" :row="row"></slot>
				</tr>
			</tbody>
		</table>

		<div class="table-footer" v-if="paginate">
			<div :class="{'datatable-length': true, 'rtl': lang.__is_rtl}">
				<label>
					<span>{{lang['rows_per_page']}}:</span>
					<select class="browser-default" @change="onTableLength">
						<option v-for="option in perPageOptions" :value="option" :selected="option == currentPerPage">
						{{ option === -1 ? lang['all'] : option }}
					  </option>
					</select>
				</label>
			</div>
			<div :class="{'datatable-info': true, 'rtl': lang.__is_rtl}">
				<span>{{(currentPage - 1) * currentPerPage ? (currentPage - 1) * currentPerPage : 1}}
					-{{Math.min(processedRows.length, currentPerPage * currentPage)}}
				</span>
				<span>
					{{lang['out_of_pages']}}
				</span>
				<span>
					{{processedRows.length}}
				</span>
			</div>
			<div>
				<ul class="material-pagination">
					<li>
						<a href="javascript:undefined" class="waves-effect btn-flat" @click.prevent="previousPage" tabindex="0">
							<i class="material-icons">chevron_left</i>
						</a>
					</li>
					<li>
						<a href="javascript:undefined" class="waves-effect btn-flat" @click.prevent="nextPage" tabindex="0">
							<i class="material-icons">chevron_right</i>
						</a>
					</li>
				</ul>
			</div>
		</div>
    </div>
    
    `,
    props: {
        title: '',
        columns: {},
        rows: {},
        clickable: {default: true},
        customButtons: {default: () => []},
        perPage: {default: () => [10, 20, 30, 40, 50]},
        defaultPerPage: {default: null},
        sortable: {default: true},
        searchable: {default: true},
        exactSearch: {
            type: Boolean,
            default: false
        },
        paginate: {default: true},
        exportable: {default: true},
        printable: {default: true},
        locale: {default: 'en'},
    },
    data: () => ({
        currentPage: 1,
        currentPerPage: 10,
        sortColumn: -1,
        sortType: 'asc',
        searching: false,
        searchInput: '',
        locales: {
            en: {
                "rows_per_page": "Rows per page",
                "out_of_pages": "of",
                "all": "All",
                "search_data": "Search data"
            }
        },
    }),
    methods: {
        nextPage: function() {
            if (this.processedRows.length > this.currentPerPage * this.currentPage)
                ++this.currentPage;
        },
        previousPage: function() {
            if (this.currentPage > 1)
                --this.currentPage;
        },
        onTableLength: function(e) {
            this.currentPerPage = parseInt(e.target.value);
        },
        sort: function(index) {
            if (!this.sortable)
                return;
            if (this.sortColumn === index) {
                this.sortType = this.sortType === 'asc' ? 'desc' : 'asc';
            } else {
                this.sortType = 'asc';
                this.sortColumn = index;
            }
        },
        search: function(e) {
            this.searching = !this.searching;
        },
        click: function(row) {
            if(!this.clickable){
                return
            }
            if(getSelection().toString()){
                // Return if some text is selected instead of firing the row-click event.
                return
            }
            this.$emit('row-click', row)
        },
        exportExcel: function() {
            const mimeType = 'data:application/vnd.ms-excel';
            const html = this.renderTable().replace(/ /g, '%20');
            const documentPrefix = this.title != '' ? this.title.replace(/ /g, '-') : 'Sheet'
            const d = new Date();
            var dummy = document.createElement('a');
            dummy.href = mimeType + ', ' + html;
            dummy.download = documentPrefix
                + '-' + d.getFullYear() + '-' + (d.getMonth()+1) + '-' + d.getDate()
                + '-' + d.getHours() + '-' + d.getMinutes() + '-' + d.getSeconds()
                +'.xls';
            document.body.appendChild(dummy);
            dummy.click();
        },
        print: function() {
            let win = window.open("");
            win.document.write(this.renderTable());
            win.print();
            win.close();
        },
        renderTable: function() {
            var table = '<table><thead>';
            table += '<tr>';
            for (var i = 0; i < this.columns.length; i++) {
                const column = this.columns[i];
                table += '<th>';
                table += 	column.label;
                table += '</th>';
            }
            table += '</tr>';
            table += '</thead><tbody>';
            for (var i = 0; i < this.rows.length; i++) {
                const row = this.rows[i];
                table += '<tr>';
                for (var j = 0; j < this.columns.length; j++) {
                    const column = this.columns[j];
                    table += '<td>';
                    table +=	this.collect(row, column.field);
                    table += '</td>';
                }
                table += '</tr>';
            }
            table += '</tbody></table>';
            return table;
        },
        dig: function(obj, selector) {
            var result = obj;
            const splitter = selector.split('.');
            for (let i = 0; i < splitter.length; i++){
                if (result == undefined)
                    return undefined;

                result = result[splitter[i]];
            }
            return result;
        },
        collect: function(obj, field) {
            if (typeof(field) === 'function')
                return field(obj);
            else if (typeof(field) === 'string')
                return this.dig(obj, field);
            else
                return undefined;
        }
    },
    computed: {
        perPageOptions: function() {
            var options = (Array.isArray(this.perPage) && this.perPage) || [10, 20, 30, 40, 50];
            // Force numbers
            options = options.map( v => parseInt(v));
            // Set current page to first value
            this.currentPerPage = options[0];
            // Sort options
            options.sort((a,b) => a - b);
            // And add "All"
            options.push(-1);
            // If defaultPerPage is provided and it's a valid option, set as current per page
            if (options.indexOf(this.defaultPerPage) > -1) {
                this.currentPerPage = parseInt(this.defaultPerPage);
            }
            return options;
        },
        processedRows: function() {
            var computedRows = this.rows;
            if (this.sortable !== false)
                computedRows = computedRows.sort((x,y) => {
                    if (!this.columns[this.sortColumn])
                        return 0;
                    const cook = (x) => {
                        x = this.collect(x, this.columns[this.sortColumn].field);
                        if (typeof(x) === 'string') {
                            x = x.toLowerCase();
                            if (this.columns[this.sortColumn].numeric)
                                x = x.indexOf('.') >= 0 ? parseFloat(x) : parseInt(x);
                        }
                        return x;
                    }
                    x = cook(x);
                    y = cook(y);
                    return (x < y ? -1 : (x > y ? 1 : 0)) * (this.sortType === 'desc' ? -1 : 1);
                })
            if (this.searching && this.searchInput) {
                const searchConfig = { keys: this.columns.map(c => c.field) }
                // Enable searching of numbers (non-string)
                // Temporary fix of https://github.com/krisk/Fuse/issues/144
                searchConfig.getFn = (obj, path) => {
                    const property = this.dig(obj, path);
                    if(Number.isInteger(property))
                        return JSON.stringify(property);
                    return property;
                }
                if(this.exactSearch){
                    //return only exact matches
                    searchConfig.threshold = 0,
                        searchConfig.distance = 0
                }
                computedRows = (new Fuse(computedRows, searchConfig)).search(this.searchInput);
            }
            return computedRows;
        },
        paginated: function() {
            var paginatedRows = this.processedRows;
            if (this.paginate)
                paginatedRows = paginatedRows.slice((this.currentPage - 1) * this.currentPerPage, this.currentPerPage === -1 ? paginatedRows.length + 1 : this.currentPage * this.currentPerPage);
            return paginatedRows;
        },
        lang: function() {
            return this.locale in this.locales ? this.locales[this.locale] : this.locales['en'];
        }
    },
    mounted: function() {
        // if (!(this.locale in locales))
        //     console.error(`vue-materialize-datable: Invalid locale '${this.locale}'`);
        this.currentPerPage = this.currentPerPage
    }
})