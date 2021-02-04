# The African microbiome portal

H3Africa initiative to provide a centralized repository for microbiome metadata associated with African populations.

## Table of Content
- [About](#about)
- [Technology](#technology)
- [Setting up the system](#setting)
- [ToDos](#todo)

<a name="about"/>

## About

The African microbiome portal (AMP) is in development under H3Africa initiative to provide a centralized repository for microbiome metadata associated with African populations, with following aims:

- To provide the most rapid and comprehensive overview of all existing African microbiome metadata.   The metadata includes sequencing details along with repository link hosting that data and  sample details including participant participant demographic details sequences repository links.
- To continuous inclusion of new newly available data, provided by authors, and acquired by publication reviewing and  other database mining.
- To establish a free, open and centralised access to harmonized publicly available African microbiome-related metadata that are interactively displayed. The metadata files will also easily downloadable as flat files from the database itself or the github repository.
- To enables submission of newly published metadata  after assessing and reviewing the submitted files following the instructions in the metadata submission guidelines section.  This will allow researchers with common scientific objectives to contribute to the scientific community by submitting and sharing their new metadata.


<a name="technology" />

## Technology

This project is created with :
- Python 3.7
- Django 2.2.7
- Liflet
- Jquery 3.3.1
- Chartjs
- Bootstrap4 4.3.1
- sqllite3

**Note**: Technology and their version might change in final version of the database.



<a name="setting"/>

## Setting up the system

The current code has onlt tested in Linux enviroment.

### Steps for Virtual Enviroment

- conda env create -f database-spec.yml
- To activate: source activate database
- To deactivate: source deactivate

### Starting the database Django server

After activating the environment using command `source activate database`

- python manage.py runserver
- Launch browser and visit [link](http://localhost:8000/microbiome/search/)

### Export dependencies of the enviroment

If you make any change in the conda environment by adding or removing modules.
```bash
conda env export --no-builds > environment2.yml
conda env export -n test-env -f test-env-spec.yml
```


<!--
# Database
Local Database For Available Data

# NOTE: Don't share sqldb

# For change tracking in django
https://stackoverflow.com/questions/37951683/how-to-track-changes-when-using-update-in-django-models

# Django relational DB Diagram from the tables

https://github.com/django-extensions/django-extensions


# Bokeh Integration in Django
https://stackoverflow.com/questions/29508958/how-to-embed-standalone-bokeh-graphs-into-django-templates/29524050#29524050

# Automated data visualisation
https://github.com/apache/incubator-superset

-->
<a name="todo"/>

## TODOs
- [ ] Create docker setting - Anmol
- [ ] Beautify file upload page - Anmol
- [ ] Back-end error correction and optimisation -- Anmol
- [ ] Cleaning of new datasets
