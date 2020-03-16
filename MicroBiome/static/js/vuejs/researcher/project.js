let EditProject = {
    name: 'edit-project',
    template: `
        <div id="content" style="margin-left: 240px;">
            <div class="row text-long-shadow text-info-filter">
                <div class="col m12 l12">
                    <p>
                        <i class="material-icons">info_outline</i> 
                        <b>Edit project {{ project.projectId }}</b>
                    </p>
                </div>
            </div>
            <div class="row">
                <form id="project-form" class="col m7" @submit="checkForm" method="post">
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
                        <div class="input-field col s12">
                            <p>1.
                                <span style="font-weight: bold;">Provide a unique project identifier</span>
                            </p>
                            <input id="project-id" class="validate" type="text" v-model="project.projectId"/>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>2.
                                <span style="font-weight: bold;">Title of project (less than 30 words)</span>
                            </p>
                            <input id="project-title" class="validate" type="text" v-model="project.projectTitle" />
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>3.
                                <span style="font-weight: bold;">Research Question (less than 1000 words)</span>
                                Please provide a <span style="font-weight: bold;">clear</span> description of the project and
                                its specific aims. Include: a. outline of the study design; b. which disease and/or control genotypes
                                you require; c. timeline; d. key references
                            </p>
                            <textarea id="research-question" class="materialize-textarea" v-model="project.researchQuestion"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>3.1
                                <span style="font-weight: bold;">For Biospecimen requests</span>
                                Please provide a <span style="font-weight: bold;">clear</span> description of a. the methodologies
                                to be used on the biospecimens; b. specific details of what you plan to do with the biospecimens.
                            </p>
                            <textarea id="biospec-methods" class="materialize-textarea" v-model="project.researchBioRequests"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>3.2
                                <span style="font-weight: bold;">For Data requests</span>
                                Please provide a <span style="font-weight: bold;">clear</span> description of a. the methodologies
                                to be used on the data; b. specific details of what you plan to do with the data.
                            </p>
                            <textarea id="data-methods" class="materialize-textarea" v-model="project.researchDataRequests"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12 file-field">
                            <p>3.3
                                <span style="font-weight: bold;">Evidence of peer review for the project</span>
                                Please attach reports of preceding peer-reviews of the study
                            </p>
                            <div class="btn h3africa">
                                <span>Reports</span>
                                <input type="file" name="reports" accept="application/pdf" id="file" multiple="multiple" />
                            </div>
                            <div class="file-path-wrapper">
                                <input class="file-path validate" type="text" placeholder="Upload one or more files"/>
                            </div>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>4.
                                <span style="font-weight: bold;">Details of data/biospecimens requested</span></p>
                            <p>4.1
                                <span style="font-weight: bold;"> For Biospecimen requests</span> The project biospecimen applied for
                            </p>
                            <textarea id="biospec-details" class="materialize-textarea" v-model="project.detailBioRequests"></textarea>
                            <p>4.2
                                <span style="font-weight: bold;"> For Data requests</span> The project data applied for
                            </p>
                            <textarea id="data-details" class="materialize-textarea" v-model="project.detailDataRequests"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>4.3
                                <span style="font-weight: bold;">Please tick the box below, if you request the associated phenotype
                            data</span>
                            </p>
                            <input id="pheno-data" type="checkbox" v-model="project.phenoDataRequested" />
                            <label for="pheno-data">Phenotype data requested</label>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12" style="margin-top: 30px">
                            <p>5.
                                <span style="font-weight: bold;">Research ethics</span>
                                Do you forsee any ethical issues, including potential harms to data subjects such as potential
                                stigmatisation of ethic groups, arising as a result of your research? If so, how do you plan to
                                address such issues?
                            </p>
                            <textarea id="research-ethics" class="materialize-textarea" v-model="project.researchEthics"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12" style="margin-top: 30px">
                            <p>6.
                                <span style="font-weight: bold;">Benefits to Africa</span>
                                The goal of the H3Africa is to improve the health of African populations, and to contribute to
                                the development of expertise and research capacity among African scientists. How do you see your
                                proposed use of the data and biospecimens contributing to this?
                            </p>
                            <textarea id="benifit-africa" class="materialize-textarea" v-model="project.benifitsAfrica"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>6.1
                                <span style="font-weight: bold;">Please list your African collaborators</span>
                                (this is required for biospecimens for the first 3 years after submission -see policy
                                document on the website)
                            </p>
                            <textarea id="collaborator-africa" class="materialize-textarea" v-model="project.africanCollaborators"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>7.
                                <span style="font-weight: bold;">Resources, Feasibility &amp; Expertise (less than 1000)</span>
                                Please describe fully your experience and expertise and that of your collaborators, wether there
                                is secured funding for your proposed use of the data and/or biospecimens, and how this will be
                                applied to the proposed study. A publication list (max 10) <span style="font-width:bold;">Must</span>
                                be provided for the applicant and co-applicants. The committee needs assurance of competence in hanging
                                datasets of this size and nature or such samples.
                            </p>
                            <textarea id="resource-feasibility" class="materialize-textarea" v-model="project.feasibility"></textarea>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12">
                            <p>8.
                                <span style="font-weight: bold;">Consent and Approvals</span>
                                Please confirm that you have obtained all approvals required for this project by the rules and
                                regulations of your jurisdiction, including your institution's institutional rules and any
                                relevant national rules, by ticking the following box: (you may be requested to provide a copy
                                of the consent form, particularly for biospecimen requests)
                            </p>
                            <p>
                                <input name="group1" id="feasibility-yes" type="radio" value="Yes" v-model="project.consentApprovals"/>
                                <label for="feasibility-yes">Yes, I obtained all approvals required</label>
                            </p>
                            <p>
                                <input name="group1" id="feasibility-no" type="radio" value="No" v-model="consentApprovalsNo"/>
                                <label for="feasibility-no">No</label>
                            </p>
                        </div>
                    </div>
                    <div class="row margin">
                        <div class="input-field col s12" style="margin-top: 30px">
                            <p>
                            <span style="font-weight: bold;">For Biospecimen requests<br/>
                            I have read and agree to abide by the terms and conditions outlined in the H3Africa Biospecimen
                            Sharing Policy and will sign the Material Transfer Agreement negotiated with the host biorepository
                            </span>
        
                            </p>
                            <p>
                                <input name="group2" id="bioagree-yes" type="radio" value="Yes" v-model="project.consentBioRequests"/>
                                <label for="bioagree-yes">Yes</label>
                            </p>
                            <p>
                                <input name="group2" id="bioagree-no" type="radio" value="No" v-model="consentBioRequestsNo"/>
                                <label for="bioagree-no">No</label>
                            </p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s12" style="margin-top: 30px">
                            <p>
                            <span style="font-weight: bold;">For Data requests<br/>
                            I have read and agree to abide by the terms and conditions outlined in the Data Access
                            Agreement and the Publication Policy?</span>
                            </p>
                            <p>
                                <input name="group3" id="dataagree-yes" type="radio" value="Yes" v-model="project.consentDataRequests"/>
                                <label for="dataagree-yes">Yes</label>
                            </p>
                            <p>
                                <input name="group3" id="dataagree-no" type="radio" value="No" v-model="consentDataRequestsNo"/>
                                <label for="dataagree-no">No</label>
                            </p>
                        </div>
                    </div>
                    <div class="divider"></div>
                    <div class="row" style="padding-top: 5px;">
                        <p>
                            <input type="submit" value="Submit">  
                        </p>
                    </div>
                </form>
                <div class="col m5">
                    <table class="bordered">
                        <thead style="background-color: #7e7e7e;">
                        <tr class="white-text">
                            <th class="white-text">Files</th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="(row, index)  in rows" :key="index" :row="row">
                            <td>{{ row }}</td>
                            <td>
                                <a class="btn red darken-2 waves-effect waves-light compact-btn" 
                                   @click="openFile(row)">
                                   <i class="material-icons white-text">file_download</i> 
                                </a>
                                <a class="btn red darken-2 waves-effect waves-light compact-btn" 
                                   @click="deleteFile(row, index)">
                                   <i class="material-icons white-text">delete</i> 
                                </a>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `,
    props: ['project', 'files'],
    data() {
        return {
            errors: [],
            rows: Object.keys(this.files),
            consentApprovalsNo: null,
            consentBioRequestsNo: null,
            consentDataRequestsNo: null
        }
    },
    methods : {
        checkForm(e) {
            e.preventDefault();
            const data = new FormData();
            let reportFiles = document.querySelector('#file');
            data.append("project", JSON.stringify(this.project));

            for (let i = 0; i < reportFiles.files.length; i++) {
                data.append("reports", reportFiles.files[i]);
            }

            this.errors = [];
            if (!this.project.projectId) {
                this.errors.push('Project Id is required');
            }
            if(this.consentApprovalsNo === 'No') {
                this.errors.push('Consent is not approved')
            }
            if(this.consentBioRequestsNo === 'No') {
                this.errors.push('Consent biospecimen request is not approved')
            }
            if(this.consentDataRequestsNo === 'No') {
                this.errors.push('Consent datasets request is not approved')
            }

            if (this.errors.length === 0) {
                let self = this;
                axios.post('/api/edit/project',
                    data, {headers: {
                            "Content-Type": "multipart/form-data"
                        }}
                ).then(function (result) {
                    self.$router.push("/advance/projects");
                })
            }
        },

        openFile(filename) {
            let path = this.files[filename];
            let url = window.location.protocol + '//' + window.location.host + '/' + path + '/' + filename;
            axios({
                // url: 'http://localhost:8080/' + path + '/' + filename,
                url: url,
                method: 'GET',
                responseType: 'blob',
            }).then(function (result) {
                const url = window.URL.createObjectURL(new Blob([result.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', filename);
                document.body.appendChild(link);
                link.click();
            });
        },

        deleteFile(filename, index) {
            let self = this;
            console.log(filename);
            let path = this.files[filename];
            let fullPath = path + '/' + filename;
            axios.post('/api/project/delete/file',
            {
                'path': fullPath
            }).then(function (result) {
                console.log(result);
                if (result.status === 200) {
                    delete self.files[filename];
                    self.rows.splice(index, 1)
                }
            })
        }
    }
};
/* ---------------------------------------------------------*
 *      PROJECTS COMPONENTS                                 *
 * ---------------------------------------------------------*/

let Project = {
    name:'project-create',
    template: `
        <div id="content" style="margin-left: 240px;">
            <div class="selected_studies_container filter-columns">
                <div class="row text-long-shadow text-info-filter">
                    <div class="col m12 l12">
                        <p>
                            <i class="material-icons">info_outline</i> 
                            <b>Create new project</b>
                        </p>
                    </div>
                </div>
                <div class="row">
                    <form id="project-form" class="col m10 push-m1" @submit="checkForm" method="post">
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
                                    <span style="font-weight: bold;">Provide a unique project identifier</span>
                                </p>
                                <input id="project-id" class="validate" type="text" v-model="dataForm.projectId"/>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>2.
                                    <span style="font-weight: bold;">Title of project (less than 30 words)</span>
                                </p>
                                <input id="project-title" class="validate" type="text" v-model="dataForm.projectTitle" />
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>3.
                                    <span style="font-weight: bold;">Research Question (less than 1000 words)</span>
                                    Please provide a <span style="font-weight: bold;">clear</span> description of the project and
                                    its specific aims. Include: a. outline of the study design; b. which disease and/or control genotypes
                                    you require; c. timeline; d. key references
                                </p>
                                <textarea id="research-question" class="materialize-textarea" v-model="dataForm.researchQuestion"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>3.1
                                    <span style="font-weight: bold;">For Biospecimen requests</span>
                                    Please provide a <span style="font-weight: bold;">clear</span> description of a. the methodologies
                                    to be used on the biospecimens; b. specific details of what you plan to do with the biospecimens.
                                </p>
                                <textarea id="biospec-methods" class="materialize-textarea" v-model="dataForm.researchBioRequests"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>3.2
                                    <span style="font-weight: bold;">For Data requests</span>
                                    Please provide a <span style="font-weight: bold;">clear</span> description of a. the methodologies
                                    to be used on the data; b. specific details of what you plan to do with the data.
                                </p>
                                <textarea id="data-methods" class="materialize-textarea" v-model="dataForm.researchDataRequests"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9 file-field">
                                <p>3.3
                                    <span style="font-weight: bold;">Evidence of peer review for the project</span>
                                    Please attach reports of preceding peer-reviews of the study
                                </p>
                                <div class="btn h3africa">
                                    <span>Reports</span>
                                    <input type="file" name="reports" accept="application/pdf" id="file" multiple="multiple" />
                                </div>
                                <div class="file-path-wrapper">
                                    <input class="file-path validate" type="text" placeholder="Upload one or more files"/>
                                </div>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>4.
                                    <span style="font-weight: bold;">Details of data/biospecimens requested</span></p>
                                <p>4.1
                                    <span style="font-weight: bold;"> For Biospecimen requests</span> The project biospecimen applied for
                                </p>
                                <textarea id="biospec-details" class="materialize-textarea" v-model="dataForm.detailBioRequests"></textarea>
                                <p>4.2
                                    <span style="font-weight: bold;"> For Data requests</span> The project data applied for
                                </p>
                                <textarea id="data-details" class="materialize-textarea" v-model="dataForm.detailDataRequests"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>4.3
                                    <span style="font-weight: bold;">Please tick the box below, if you request the associated phenotype
                                data</span>
                                </p>
                                <input id="pheno-data" type="checkbox" v-model="dataForm.phenoDataRequested" />
                                <label for="pheno-data">Phenotype data requested</label>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9" style="margin-top: 30px">
                                <p>5.
                                    <span style="font-weight: bold;">Research ethics</span>
                                    Do you forsee any ethical issues, including potential harms to data subjects such as potential
                                    stigmatisation of ethic groups, arising as a result of your research? If so, how do you plan to
                                    address such issues?
                                </p>
                                <textarea id="research-ethics" class="materialize-textarea" v-model="dataForm.researchEthics"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9" style="margin-top: 30px">
                                <p>6.
                                    <span style="font-weight: bold;">Benefits to Africa</span>
                                    The goal of the H3Africa is to improve the health of African populations, and to contribute to
                                    the development of expertise and research capacity among African scientists. How do you see your
                                    proposed use of the data and biospecimens contributing to this?
                                </p>
                                <textarea id="benifit-africa" class="materialize-textarea" v-model="dataForm.benifitsAfrica"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>6.1
                                    <span style="font-weight: bold;">Please list your African collaborators</span>
                                    (this is required for biospecimens for the first 3 years after submission -see policy
                                    document on the website)
                                </p>
                                <textarea id="collaborator-africa" class="materialize-textarea" v-model="dataForm.africanCollaborators"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>7.
                                    <span style="font-weight: bold;">Resources, Feasibility &amp; Expertise (less than 1000)</span>
                                    Please describe fully your experience and expertise and that of your collaborators, wether there
                                    is secured funding for your proposed use of the data and/or biospecimens, and how this will be
                                    applied to the proposed study. A publication list (max 10) <span style="font-width:bold;">Must</span>
                                    be provided for the applicant and co-applicants. The committee needs assurance of competence in hanging
                                    datasets of this size and nature or such samples.
                                </p>
                                <textarea id="resource-feasibility" class="materialize-textarea" v-model="dataForm.feasibility"></textarea>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9">
                                <p>8.
                                    <span style="font-weight: bold;">Consent and Approvals</span>
                                    Please confirm that you have obtained all approvals required for this project by the rules and
                                    regulations of your jurisdiction, including your institution's institutional rules and any
                                    relevant national rules, by ticking the following box: (you may be requested to provide a copy
                                    of the consent form, particularly for biospecimen requests)
                                </p>
                                <p>
                                    <input name="group1" id="feasibility-yes" type="radio" value="Yes" v-model="dataForm.consentApprovals"/>
                                    <label for="feasibility-yes">Yes, I obtained all approvals required</label>
                                </p>
                                <p>
                                    <input name="group1" id="feasibility-no" type="radio" value="No" v-model="consentApprovalsNo"/>
                                    <label for="feasibility-no">No</label>
                                </p>
                            </div>
                        </div>
                        <div class="row margin">
                            <div class="input-field col s9" style="margin-top: 30px">
                                <p>
                                <span style="font-weight: bold;">For Biospecimen requests<br/>
                                I have read and agree to abide by the terms and conditions outlined in the H3Africa Biospecimen
                                Sharing Policy and will sign the Material Transfer Agreement negotiated with the host biorepository
                                </span>
            
                                </p>
                                <p>
                                    <input name="group2" id="bioagree-yes" type="radio" value="Yes" v-model="dataForm.consentBioRequests"/>
                                    <label for="bioagree-yes">Yes</label>
                                </p>
                                <p>
                                    <input name="group2" id="bioagree-no" type="radio" value="No" v-model="consentBioRequestsNo"/>
                                    <label for="bioagree-no">No</label>
                                </p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="input-field col s9" style="margin-top: 30px">
                                <p>
                                <span style="font-weight: bold;">For Data requests<br/>
                                I have read and agree to abide by the terms and conditions outlined in the Data Access
                                Agreement and the Publication Policy?</span>
                                </p>
                                <p>
                                    <input name="group3" id="dataagree-yes" type="radio" value="Yes" v-model="dataForm.consentDataRequests"/>
                                    <label for="dataagree-yes">Yes</label>
                                </p>
                                <p>
                                    <input name="group3" id="dataagree-no" type="radio" value="No" v-model="consentDataRequestsNo"/>
                                    <label for="dataagree-no">No</label>
                                </p>
                            </div>
                        </div>
                        <div class="divider"></div>
                        <div class="row" style="padding-top: 5px;">
                            <p>
                                <input type="submit" value="Submit">  
                            </p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    `,
    data() {
        return {
            errors:[],
            consentApprovalsNo: null,
            consentBioRequestsNo: null,
            consentDataRequestsNo: null,
            dataForm: {
                projectId: null,
                projectTitle: null,
                researchQuestion: null,
                researchBioRequests: null,
                researchDataRequests: null,
                detailBioRequests: null,
                detailDataRequests: null,
                phenoDataRequested: null,
                researchEthics: null,
                benifitsAfrica: null,
                africanCollaborators: null,
                feasibility: null,
                consentApprovals: null,
                consentBioRequests: null,
                consentDataRequests: null
            },
            reports: []
        }
    },
    methods: {
        checkForm(e) {
            e.preventDefault();
            const data = new FormData();
            let reportFiles = document.querySelector('#file');
            data.append("project", JSON.stringify(this.dataForm));
            // data.append("reports", imagefile.files[0]);
            for (let i = 0; i < reportFiles.files.length; i++) {
                data.append("reports", reportFiles.files[i]);
            }
            this.erros = [];
            if (!this.dataForm.projectId) {
                this.errors.push('Project Id required');
            }

            if (this.erros.length === 0) {
                let self = this;
                axios.post('/api/create/project',
                    data, {headers: {
                        "Content-Type": "multipart/form-data"
                    }}
                ).then(function (result) {
                    self.$router.push("/advance/projects");
                })
            }
        }
    }
};

/*---------------------------------------------------------*
 *   A cards has a project information, number of pending  *
 *   and approved carts                                   *
 *---------------------------------------------------------*/

let ProjectCard = {
    template: `
        <div class="card z-depth-0" v-if="card" v-bind:style="{opacity: opacity}">
            <div class="card-image h3africa waves-effect">
                <div class="card-title">{{ projectId }}</div>
                <div class="price">{{ cardLength }}</div>
                <div class="price-desc">Carts</div>
            </div>
            <div class="card-content">
                <ul class="collection">
                    <li class="collection-item">
                        <span>Pending</span> 
                        <span class="task-cat grey darken-3 right" 
                            style="font-weight: bold;padding: 0 10px;font-size: 16px;">{{ pendingLength }}</span>
                    </li>
                    <li class="collection-item">
                        <span>Requested</span> 
                        <span class="task-cat grey darken-3 right" 
                            style="font-weight: bold;padding: 0 10px;font-size: 16px;">{{ requestedLength }}</span>
                    </li>
                    <li class="collection-item">
                        <span>Approved</span> 
                        <span class="task-cat grey darken-3 right"
                            style="font-weight: bold;padding: 0 10px;font-size: 16px;">{{ approvedLength }}</span>
                    </li>
                </ul>
            </div>
            <div class="card-action center-align">                      
                <button class="waves-effect waves-light btn blue-grey" @click="editProject">
                    <i class="material-icons">edit</i>
                </button>
                <button class="waves-effect waves-light btn blue-grey" @click="selectProject">
                    <i class="material-icons">check</i>
                </button>
                <button class="waves-effect waves-light btn blue-grey" @click="deleteProject">
                    <i class="material-icons">delete</i>
                </button>
            </div>
        </div>
    `,
    props: ['card', 'selectedProjectId'],
    computed: {
        projectId() {
            return this.card.project.projectId
        },
        cardLength() {
            return this.card['pending-cards'].length +
                this.card['requested-cards'].length +
                this.card['approved-cards'].length
        },
        pendingLength() {
            return this.card['pending-cards'].length
        },
        requestedLength() {
            return this.card['requested-cards'].length
        },
        approvedLength() {
            return this.card['approved-cards'].length
        },
        opacity() {
            if (this.projectId === this.selectedProjectId) {
                return 0.7
            }
            return 1
        }
    },
    methods: {
        editProject: function (e) {
            let self = this;
            axios.get(
                `/api/project/edit/${this.projectId}`
            ).then(function (result) {
                self.$router.push({name: 'edit-project', params: {project: result.data.project, files: result.data.files}});
            })
        },
        selectProject: function (e) {
            this.$emit('card-selected', this.projectId)
        },
        deleteProject: function (e) {
            let self = this;
            axios.get(
                `/api/remove/${this.projectId}`
            ).then(function (result) {
                if (result.data.error) {
                    alert(result.data.error);
                } else {
                    self.$emit('card-deleted');
                }
            });
        }
    }
};

let ProjectCards = {
    template: `
        <section id="content" style="margin-left: 240px;">
            <div class="container">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <h5 class="breadcrumbs-title">Your Projects</h5>
                        <ol class="breadcrumbs">
                            <li><a href="/" style="color: #00bcd4;">Home</a></li>
                            <li class="active">Projects</li>
                        </ol>
                    </div>
                </div>
            </div>
            <div class="container">
                <p class="caption">
                    Create, edit, select and delete projects
                </p>
                <div class="divider"></div>
                <div class="row text-long-shadow text-info-filter" style="margin: 1rem 0.1rem">
                    <div class="col m8 l8">
                        <p v-if="selectedProjectId == null">
                            <i class="material-icons">warning</i>
                            <span class="project-selected">Click on<i class="material-icons">check</i> to select a project.</span>
                        </p>
                        <p v-else>
                            <span class="project-selected">Project 
                                <span class="task-cat teal">
                                {{ selectedProjectId }}</span> is selected.</span>
                        </p>
                    </div>
                    <div class="col m4 l4">
                        <router-link tag="button" to="/advance/projects/project"
                                     class="btn waves-effect waves-light blue-grey right">
                            <i class="material-icons">add</i> Create Project
                        </router-link>
                    </div>
                </div>
                    
                <div class="row">
                    <section id="plans" class="plans-container" v-for="i in loopLength">
                        <article class="col s12 m4 l4" v-for="j in 3">
                            <x-project-card :card="cards[(i-1)*3+j-1]" 
                                            :selected-project-id="selectedProjectId" 
                                            @card-selected="setProjectId" 
                                            @card-deleted="cardDeleted"></x-project-card>
                        </article>
                    </section>
                </div>
            </div>
        </section>
    `,
    props: ['cards', 'selectedProjectId'],
    data() {
        return {
            username: state.user.name
        }
    },
    computed: {
        loopLength() {
            return Math.floor((this.cards.length -1) / 3 + 1);
        }
    },
    components: {
        'x-project-card': ProjectCard
    },
    methods: {
        setProjectId(projectId) {
            this.$emit('card-selected', projectId);
        },
        cardDeleted() {
            this.$parent.getProjects();
        }
    }
};

let Projects = {
    name: 'projects',
    template: '#user-projects',
    data() {
        return {
            cards: projectState.cards,
            selectedProjectId: state.projectId
        }
    },
    components: {
        'x-project-cards': ProjectCards
    },
    methods: {
        setCards(cards) {
            this.cards = cards;
        },
        setProjectId(projectId) {
            if (this.selectedProjectId === projectId) {
                this.selectedProjectId = null;
                state.selectedCart = null;
                state.selectedRows = null;
                state.nbRowSelected = 0;
            } else {
                this.selectedProjectId = projectId;
            }

            this.$parent.setProjectId(this.selectedProjectId);
        },
        getProjects() {
            var self = this;
            axios.get('/api/projects')
                .then(function (result) {
                    self.setCards(result.data['project-cards']);
                })
        }
    },
    created() {
        this.getProjects();
    }
};
