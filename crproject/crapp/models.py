from django.db import models

class Kitchen(models.Model):
	length=models.FloatField(default=0.0)
	width=models.FloatField(default=0.0)
	cost =models.FloatField(default=0.0)

class Bedroom(models.Model):
	length=models.FloatField(default=0.0)
	width=models.FloatField(default=0.0)
	cost=models.FloatField(default=0.0)

class Hall(models.Model):
	length=models.FloatField(default=0.0)
	width=models.FloatField(default=0.0)
	cost =models.FloatField(default=0.0)
	
class Handles(models.Model):
	name = models.CharField(max_length=512,null=True, blank=True)
	photos = models.TextField(default="data:image/jpeg;base64,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")
	price =models.FloatField(default=1000.0)
	totalprice =models.FloatField(default=0.0)
	quantity = models.IntegerField(default=1)
	#kitchen = models.ForeignKey(Kitchen, default=1, on_delete=models.CASCADE)
	#bedroom = models.ForeignKey(Bedroom, default=1, on_delete=models.CASCADE)
	#hall = models.ForeignKey(Hall,default=1, on_delete=models.CASCADE)

class Doors(models.Model):
	name = models.CharField(max_length=512,null=True, blank=True)
	photos = models.TextField(default="data:image/jpeg;base64,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")
	price =models.FloatField(default=1000.0)
	totalprice =models.FloatField(default=0.0)
	quantity = models.IntegerField(default=1)
	#kitchen = models.ForeignKey(Kitchen,default=1, on_delete=models.CASCADE)
	#bedroom = models.ForeignKey(Bedroom,default=1, on_delete=models.CASCADE)
	#hall = models.ForeignKey(Hall, default=1, on_delete=models.CASCADE)
