from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Snipit
from django.contrib import messages
# from .forms import SnipitForm

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


def edit(request,snip_id):
#     form= UserForm(request.POST or None)

#     if form.is_valid():
#         data= form.cleaned_data.get("form_field")

        if request.method == "PUT": 
                language_name =request.PUT["language_name"]
                snip_title=request.PUT["snip_title"]
                language_code= request.PUT["language_code"]
                short_description= request.PUT["short_description"]
                snipitt = Snipit(language_name=language_name,snip_title=snip_title,language_code=language_code,short_description=short_description)
                snipitt.save()
                messages.info(request, "successfully saved snipt")
                return redirect("users/index.html")
        else:

                Selected_snip = Snipit.objects.get(id=snip_id)
        return render( request, "users/edit.html",{"navbar":"edit","viw_snip":Selected_snip})             
        
        
# "header": 'with c# ',