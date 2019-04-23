from django import forms

from .models import Project


class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("country",)
        #  fields = ("collection_date", 'platform', "amplicon_target",
        #            "isolation_source", "country", "special_diet")
