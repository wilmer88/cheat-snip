from django.shortcuts import render
from django.http import HttpResponse

def index(request):

       return render(request, "users/index.html", {
        "things_to_do": ["learn c", 'learn python', 'find work']})
        
def fight_stage(request):
        return render(request, 'users/fight_stage.html', {})
        
        
# "header": 'with c# ',