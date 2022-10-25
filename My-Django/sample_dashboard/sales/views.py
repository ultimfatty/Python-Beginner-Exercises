from django.shortcuts import render
import pandas as pd

def index(request):
    return render(request, 'index.html')


