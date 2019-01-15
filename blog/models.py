from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class materials(models.Model):
	name=models.ForeignKey('MEbelda',on_delete=models.CASCADE)
	basicTkan=models.IntegerField('основная ткань')
	tkanCompanion=models.IntegerField('компаньон ткани')
	podushki=models.IntegerField('подушки')
	sizesOfPruzhinBlock=models.IntegerField('размеры пружинных блоков')
	dsp=models.IntegerField('ДСП')
	dvp=models.IntegerField('ДВП')
	dvpo=models.IntegerField('ДВПО')
	brus=models.CharField('размеры бруса',max_length=300)
	porolon=models.CharField('размеры поролона',max_length=300)
	oporaChrome=models.CharField('опора хром',max_length=200)
	lockers=models.CharField('замки',max_length=200)
	
	def create(self):
		self.save()
	def __str__(self):
		return self.lockers
	def as_json(self):
		d = {self._meta.get_field(i).verbose_name:[getattr(self,i),i] for i in [j for j in dir(self) if '_' not in j and j not in {'name','DoesNotExist','MultipleObjectsReturned','author','check','clean','id','create','delete','objects','pk','save'}]}
		for i in d:
			if type(self._meta.get_field(d[i][1])) is models.DateField:
				d[i][1]=0
			elif type(self._meta.get_field(d[i][1])) is models.CharField:
				d[i][1]=1
			else:
				d[i][1]=2
		return d
		
		
class MEbelda(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	name=models.CharField('наименование',max_length=200)
	price=models.DecimalField('цена',max_digits=8,decimal_places=2)
	prepay=models.DecimalField('предоплата',max_digits=8,decimal_places=2)
	ostatok=models.DecimalField('остаток',max_digits=8,decimal_places=2)
	priceForProvide=models.DecimalField('цена за доставку',max_digits=8,decimal_places=2)
	priceForUp=models.DecimalField('цена за подъём',max_digits=8,decimal_places=2)
	oformDate=models.DateField('дата оформления')
	postDate=models.DateField('дата поставки')
	basicTkan=models.CharField('основная ткань',max_length=200)
	tkanCompanion=models.CharField('компаньон ткани',max_length=200)
	podushColor=models.CharField('расцветка подушек',max_length=200)
	clientAddress=models.CharField('адрес клиента',max_length=200)
	clientPhone=models.IntegerField('телефонный номер клиента')
	commentaries=models.CharField('комментарии',max_length=1000)
	customFields=models.TextField()
	done=models.BooleanField(default=False)
	has_cancel=models.BooleanField(default=False)
	have_shab=models.BooleanField(default=False)
	
	def create(self):
		self.save()
	def __str__(self):
		return self.name
	def as_json(self):
		d = {self._meta.get_field(i).verbose_name:[getattr(self,i),i] for i in [j for j in dir(self) if '_' not in j and j not in {'customFields','DoesNotExist','done','MultipleObjectsReturned','author','check','clean','id','create','delete','objects','pk','save'}]}
		for i in d:
			if type(self._meta.get_field(d[i][1])) is models.DateField:
				d[i][1]=0
			elif type(self._meta.get_field(d[i][1])) is models.CharField:
				d[i][1]=1
			else:
				d[i][1]=2
		return d

		

class Mebel(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	basic_material = models.IntegerField()
	
	def create(self):
		self.save()
	
	def __str__(self):
		return self.name
		
	def as_json(self):
		return dict(name=self.name,basic_materials=self.basic_material)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
class data(models.Model):
	time = datetime.datetime.now().strftime('%d_%m_%Y_%H:%M:%S')
	text = models.TextField()
	def ins(self):
		self.save()
		
class tesmebel(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	basic_material = models.IntegerField
	def create(self):
		self.save()
		
class tes1mebel(models.Model):
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	basic_material = models.IntegerField
	def create(self):
		self.save()
		
class test(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	basic_material = models.IntegerField()
	
	def create(self):
		self.save()
	
	def __str__(self):
		return self.name