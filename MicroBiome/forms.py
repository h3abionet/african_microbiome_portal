from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from django.urls import reverse

from .models import Tags

# class Upload(forms.Form):
# infile = forms.FileField()
# separator = forms.ChoiceField(
# choices=(
# ("", "Choose ...."),
# (" ", "Space"),
# ("\t", "Tab"),
# (",", "Comma"),
# (";", "Semi-Comma"),
# )
# )

# def __init__(self, *args, **kwargs):
# super(Upload, self).__init__(*args, **kwargs)
# self.helper = FormHelper(self)
# self.helper.form_action = reverse("upload")
# self.helper.method = "POST"
#  self.fields["infile"].label = False
#  self.helper.form_show_labels = False
#  selff.helper.layout = Layout(
#      Row(Column('infile', css_class='form-group col-md-4 mb-0'),
#          Column('separator', css_class='form-group col-md-4 mb-0')
#          )
#  )


class PostForm(forms.ModelForm):
    #  tags = forms.CharField(label='')
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["tags"].label = ""

    class Meta:
        model = Tags
        #  fields = ("country",)
        #  fields = ("country", "platform", "disease", "study_design")
        fields = ("tags", )
        widgets = {
            "tags":
            forms.TextInput(
                attrs={  # 'data-role': 'tagsinput',
                    #  'class':'form-control',
                    "type": "text",
                    "placeholder":
                    "(Malawi[country] & AMPLICON[assay]) | ~Eye[bodysite]",
                    "value":
                    "(Malawi[country] & AMPLICON[assay]) | ~Eye[bodysite]"
                })
        }
        error_css_class = "error"
        required_css_class = "bold"
        # https://www.webforefront.com/django/formtemplatelayout.html
        # TODO: allow empty fields

    #  def clean_rowname(self):
    #      return self.cleaned_data['country'] or None


# https://django-autocomplete-light.readthedocs.io/en/master/tutorial.html
# https://medium.com/@viewflow/redesigning-an-autocomplete-for-django-1994fd07c0a6
