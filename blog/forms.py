from django import forms
from drf_braces.serializers.form_serializer import FormSerializer
from .models import data
from .models import tesmebel
from .models import tes1mebel
from .models import Mebel
from django.contrib.auth.forms import UserCreationForm

class MebelForm(forms.ModelForm):
	class Meta:
		model = Mebel
		fields = ('name','basic_material',)
		
class MebelSerial(FormSerializer):
	class Meta(object):
		form = MebelForm

class tochange(forms.ModelForm):
	class meta:
		model = data
		fields = ('text',)

class tesmebelForm(forms.ModelForm):
	class meta:
		model = tesmebel
		fields = ('name','basic_material',)
		
class tes1mebelForm(forms.ModelForm):
	class meta:
		model = tes1mebel
		fields = ('name','basic_material',)