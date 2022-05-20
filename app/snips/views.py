from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
      
        return render(request, "cheatCode/home.html", {"header": 'with c# ',
        "things_to_do": ["learn c", 'learn python', 'find work']})
        
def fight_stage(request):
        
        return render(request, 'cheatCode/fight_stage.html', {})
