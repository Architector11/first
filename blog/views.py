from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from django.shortcuts import render
from django.http import JsonResponse
from .forms import tochange
from .models import Mebel
from .models import MEbelda,materials
import json


def doc(request):
	d = tochange(request.POST)
	d.ins()
	return JsonResponse({"1":1},status=201)
def post_list(request):
	return render(request,'blog/post_list.html',{})
def test(requests):
	response = {"a":1,"b":2}
	return JsonResponse(response,status=201)
	
class RegisterFormView(FormView):
	form_class=UserCreationForm
	success_url="/login/"
	template_name="register.html"
	def form_valid(self,form):
		form.save()
		return super(RegisterFormView,self).form_valid(form)
		
class LoginFormView(FormView):
	form_class = AuthenticationForm
	template_name="login.html"
	success_url="/"
	def form_valid(self,form):
		self.user=form.get_user()
		login(self.request,self.user)
		return super(LoginFormView,self).form_valid(form)
		
def logout_view(request):
	logout(request)
	return render(request,'logged_out.html',{})
	
def zakazy(request):
	if request.user.is_authenticated:
		meb=MEbelda.objects.filter(author=request.user).filter(done=False)
		if len(meb)!=0:
			r = []
			for i in meb:
				r.append([i.as_json(),materials.objects.get(name=i).as_json()])
			return JsonResponse({"response":r},status=201)
		else:
			return JsonResponse({"response":"none"},status=201)
	else:
		return JsonResponse({"response":"err_auth"},status=201)
			
def history(request):
	if request.user.is_authenticated:
		meb=MEbelda.objects.filter(author=request.user).filter(done=True)
		if len(meb)!=0:
			r=[]
			for i in meb:
				#r.append([i.as_json(),materials.objects.get(name=i).as_json()])
				tmp=[i.as_json(),materials.objects.get(name=i).as_json()]
				tmp[0]['canc']=i.has_cancel
				r.append(tmp)
			return JsonResponse({"response":r},status=201)
		else:
			return JsonResponse({"response":"none"},status=201)
	return JsonResponse({"response":"zaglushka_for_histotry"},status=201)
	
def to_shab(request):
	if request.user.is_authenticated:
		req=request.POST.dict()
		a = MEbelda.objects.filter(author=request.user).get(name=req['name'])
		a.have_shab=True
		a.save()
		#tmp=a.as_json()
		#b = {i:tmp[i] for i in tmp if i not in names}
		#print(b)
		return JsonResponse({"response":"shablon created"},status=201)
	else:
		return JsonResponse({"response":"err_auth"},status=201)
		
def delete_shab(request):
	if request.user.is_authenticated:
		req=request.POST.dict()
		a = MEbelda.objects.filter(author=request.user).get(name=req['name'])
		a.have_shab=False
		a.save()
		return JsonResponse({"response":"shablon success deleted"},status=201)
	else:
		return JsonResponse({"response":"err_auth"},status=201)
		
def names(request):
	if request.user.is_authenticated:
		a = MEbelda.objects.all()
		if len(a)!=0:
			for i in a:
				b = {i.name:1 for i in a}
			return JsonResponse({"response":b},status=201)
		else:
			return JsonResponse({"response":'none'},status=201)
	else:
		return JsonResponse({"response":"err_auth"},status=201)
		
def create(request):
	if request.user.is_authenticated:
		req=request.POST.dict()
		print(req,'\n')
		a={}
		b={}
		for i in req:
			if 'basic' in i:
				a[i.split('[')[1].replace(']','')]=req[i]
			elif 'mat' in i:
				b[i.split('[')[1].replace(']','')]=req[i]
				
		MEbelda.objects.create(author=request.user,name=a['наименование'],price=a['цена'],prepay=a['предоплата'],ostatok=a['остаток'],priceForProvide=a['цена за доставку'],priceForUp=a['цена за подъём'],oformDate=a['дата оформления'],postDate=a['дата поставки'],basicTkan=a['основная ткань'],tkanCompanion=a['компаньон ткани'],podushColor=a['расцветка подушек'],clientAddress=a['адрес клиента'],clientPhone=a['телефонный номер клиента'],commentaries=a['комментарии'])
		did=MEbelda.objects.filter(author=request.user).get(name=a['наименование'])
		materials.objects.create(name=did,basicTkan=b['основная ткань'],tkanCompanion=b['компаньон ткани'],podushki=b['подушки'],sizesOfPruzhinBlock=b['размеры пружинных блоков'],dsp=b['ДСП'],dvp=b['ДВП'],dvpo=b['ДВПО'],brus=b['размеры бруса'],porolon=b['размеры поролона'],oporaChrome=b['опора хром'],lockers=b['замки'])
		return JsonResponse({"response":"zakaz success created"},status=201)
	else:
		return JsonResponse({"response":"err_auth"},status=201)
		
def shablony(request):
	if request.user.is_authenticated:
		names = {'адрес клиента','телефонный номер клиента','комментарии','дата оформления','остаток','дата поставки','предоплата','цена за доставку','цена за подъём'}
		a = MEbelda.objects.filter(author=request.user).filter(have_shab=True)
		if len(a)!=0:
			r = []
			for i in a:
				tmp=i.as_json()
				#r.append([{j:tmp[j] for j in tmp if j not in names else j},materials.objects.get(name=i).as_json()])
				r.append([{j:tmp[j] if j not in names else ['AAA',tmp[j][1]] for j in tmp},materials.objects.get(name=i).as_json()])
				#print(tmp)
			return JsonResponse({"response":r},status=201)
		else:
			return JsonResponse({"response":"none"},status=201)
	else:
		return JsonResponse({"response":"err_auth"},status=201)
			
def update(request):
	if request.user.is_authenticated:
		req=request.POST.dict()
		try:
			if req['to_history']=='true' and req['canc']=='false':
				a=MEbelda.objects.filter(author=request.user).get(name=req['name'])
				a.done=True
				a.save()
				return JsonResponse({"response":"success delete"},status=201)
			elif req['to_history']=='true' and req['canc']=='true':
				print('/////////////////////','\n',req)
				a=MEbelda.objects.filter(author=request.user).get(name=req['name'])
				a.done=True
				a.has_cancel=True
				a.save()
				return JsonResponse({"response":"success delete"},status=201)
			else:
				a=MEbelda.objects.filter(author=request.user).get(name=req['name'])
				b=materials.objects.get(name=a)
				fields=[i for i in dir(a) if '_' not in i and i not in {'name','DoesNotExist','done','MultipleObjectsReturned','author','check','clean','id','create','delete','objects','pk','save'}]
				f_and_v={a._meta.get_field(i).verbose_name:i for i in fields}
				fields_m=[i for i in dir(b) if '_' not in i and i not in {'name','DoesNotExist','done','MultipleObjectsReturned','author','check','clean','id','create','delete','objects','pk','save'}]
				for i in fields_m:
					f_and_v[b._meta.get_field(i).verbose_name]=i
				for i in req:
					if 'base' in i:
						setattr(a,f_and_v[i.split('[0]')[1].replace('[','').replace(']','')],req[i])
					elif 'materials' in i:
						setattr(b,f_and_v[i.split('[0]')[1].replace('[','').replace(']','')],req[i])
				a.save()
				b.save()
				return JsonResponse({"response":"success saved"},status=201)
		except:
			return JsonResponse({"response":"invalid request"},status=201)
			
			
	
		
'''class LogoutView(View):
	def get(self,request):
		logout(request)
		return HttpResponseRedirect('logout')'''
		
#def login(request):
#	return render(request,'login.html',{})