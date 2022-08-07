from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.
class Snipit(models.Model):
    language_name = models.CharField(max_length=240, blank=False, null=False)
    snip_title = models.CharField(max_length=240, blank=False, null=False)
    language_code = models.CharField(max_length=2000, blank=False, null=False)
    short_description = models.CharField(max_length=240,blank=False, null=False)
class Meta:
    db_table = "snipit"    
    def __str__(self):
        """A human readible representation of user object"""
        return "{0} {1} {2} {3}".format(self.language_name, self.snip_title, self.language_code, self.short_description)
    

