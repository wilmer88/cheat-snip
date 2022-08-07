from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Snipit
from django.contrib import messages
# from .forms import SnipitForm
from snips.forms import SnipitForm

# monkey= datetime.datetime.now()
def index(request):
       all_snips = Snipit.objects.all()     
       return render(request, "users/index.html", {
               "navbar":"index", "language": all_snips
  })
        
def fight_stage(request):
        return render(request, 'users/fight_stage.html', {})

def add_snip(request):
        # snipForm = SnipitForm()
        if request.method == "POST": 
                language_name =request.POST["language_name"]
                snip_title=request.POST["snip_title"]
                language_code= request.POST["language_code"]
                short_description= request.POST["short_description"]
                snipit = Snipit(language_name=language_name,snip_title=snip_title,language_code=language_code,short_description=short_description)
                snipit.save()
            
              
                messages.info(request, "successfully saved snipt")
                return redirect("users/index.html")
               
        return render(request, "users/add_snip.html", {
                
                "navbar":"add_snip"
                })


def edit(request,id):
 Selected_snip = Snipit.objects.get(id=id)
 forms = SnipitForm(request.POST, instance=Selected_snip)
 if forms.is_valid():
        forms.save()
 return render(request, "users/edit.html",{"navbar":"edit","viw_snip":Selected_snip}) 

      