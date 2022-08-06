from django.shortcuts import render
from django.http import HttpResponse
from .models import Snipit
# monkey= datetime.datetime.now()
def index(request):
     
        all_snips = Snipit.objects.all()

        return render(request, "users/index.html", {
               "navbar":"index", "language": all_snips
  })
        
def fight_stage(request):
        return render(request, 'users/fight_stage.html', {})

def add_snip(request):
        return render(request, "users/add_snip.html", {
                "navbar":"add_snip"
                })
def edit(request):
        return render(request, "users/edit.html", {
                "navbar":"edit"
                })                
        
        
# "header": 'with c# ',