import numpy as np
import pandas as pd

# For pagination
#  from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Q, Sum
from django.db.models.functions import Length
from django.shortcuts import redirect
from django.shortcuts import render
# from django.shortcuts import render_to_response
from django_pandas.io import read_frame
from django.views.decorators.csrf import csrf_exempt

#  from django_tables2.config import RequestConfig
#  from .djmodel import get_model_repr
# Create your views here.
#  from .models import Movie, Person
from .forms import PostForm, Upload
from .models import (Amplicon, Assay, Disease, LocEthDiet, Platform, Project,
                     Samples, TestProject)


def search(request):
    if request.method=="POST":
        search_text = request.POST["tags"]
    else:
        search_text = ''
    print("Varsha Shetty", request.POST['oldsearch'])
    if search_text=='':
        res = pd.DataFrame()
    else:
        res = read_frame(TestProject.objects.filter(title__icontains=search_text))
    print(res)

    return render(None,"ajax_search.html",{'results':res})
