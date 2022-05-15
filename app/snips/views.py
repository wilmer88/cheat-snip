from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
        response = "<h1> django is working</h1>"
        return HttpResponse(response)
        
def fight_stage(request):
        response = """<h1> fight stage will be on this page</h1>"""
        return HttpResponse(response)
