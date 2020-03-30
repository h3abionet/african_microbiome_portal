# Virtual Enviroment

- conda env create -f database-spec.yml
- To activate: source activate database
- To deactivate: source deactivate


# Export dependencies of the enviroment

```bash
conda env export --no-builds > environment2.yml
conda env export -n test-env -f test-env-spec.yml
```



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



# TODOs
- [ ] Update dependencies for installation - Anmol
- [ ] Create docker - Anmol
- [ ] Add footers. - Micheal
- [ ] Fix orientation of dashboard - Micheal
- [ ] Fix orientations of data test page -  Alfred
	- Highlight data already existing data in the database
- [ ] Add map in data test page -- Anmol
- [ ] Accordion help page -- Anmol
- [ ] Beautify file upload page - Anmol
- [ ] Back-end error correction and optimisation -- Anmol
- [ ] There is also no link to the corresponding study (pubmed)
