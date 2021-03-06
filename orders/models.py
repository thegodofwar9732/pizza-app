from django.db import models

# Create your models here.
class Style(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=15)

	def __str__(self):
		return self.name


class Size(models.Model):
	size = models.CharField(max_length=5)
	def __str__(self):
		return self.size


class Topping(models.Model):
	name = models.CharField(max_length=16)
	price = models.DecimalField(max_digits=4, decimal_places=2, default=0.50)
	

	def __str__(self):
		return self.name


class Pizza(models.Model):
	isMenu = models.BooleanField(default=True)
	user = models.CharField(max_length=15, blank=True)
	pizza = models.ForeignKey(Style, on_delete=models.CASCADE, related_name="pizza")
	items = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="pizza")
	size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="pizza")
	price = models.DecimalField(max_digits=4, decimal_places=2)
	toppings = models.ManyToManyField(Topping, blank=True)

	def topping_set(self):
		return self.toppings.all()
	

	def __str__(self):
		return f"{self.size} {self.pizza} {self.items} Menu: {self.isMenu}"


class SubKind(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name


class Sub(models.Model):
	isMenu = models.BooleanField(default=True)
	user = models.CharField(max_length=15, blank=True)
	kind = models.ForeignKey(SubKind, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=4, decimal_places=2, default=6.50)

	def __str__(self):
		return f"{self.size}  {self.kind} Sub Menu: {self.isMenu}"


class Pasta(models.Model):
	isMenu = models.BooleanField(default=True)
	user = models.CharField(max_length=15, blank=True)
	name = models.CharField(max_length=25)
	price = models.DecimalField(max_digits=4, decimal_places=2, default=6.50)
	def __str__(self):
		return f"{self.name} Menu: {self.isMenu}"

class Salad(models.Model):
	isMenu = models.BooleanField(default=True)
	user = models.CharField(max_length=15, blank=True)
	name = models.CharField(max_length=25)
	price = models.DecimalField(max_digits=4, decimal_places=2, default=6.25)
	def __str__(self):
		return f"{self.name} Menu: {self.isMenu}"

class Dinner_Platter(models.Model):
	isMenu = models.BooleanField(default=True)
	user = models.CharField(max_length=15, blank=True)
	name = models.CharField(max_length=25)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=4, decimal_places=2, default=35)
	def __str__(self):
		return f"{self.size} {self.name} Menu: {self.isMenu}"


class Cart(models.Model):
	user = models.CharField(max_length=15, blank=True)
	pizzas = models.ManyToManyField(Pizza, blank=True)
	subs = models.ManyToManyField(Sub, blank=True)
	pastas = models.ManyToManyField(Pasta, blank=True)
	salads = models.ManyToManyField(Salad, blank=True)
	platters = models.ManyToManyField(Dinner_Platter, blank=True)
	total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)

	def __str__(self):
		return self.user +"'s Cart"

class Order(models.Model):
	user = models.CharField(max_length=15, blank=True)
	pizzas = models.ManyToManyField(Pizza, blank=True)
	subs = models.ManyToManyField(Sub, blank=True)
	pastas = models.ManyToManyField(Pasta, blank=True)
	salads = models.ManyToManyField(Salad, blank=True)
	platters = models.ManyToManyField(Dinner_Platter, blank=True)
	total = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)

	def __str__(self):
		return self.user +"'s Order"


# models must be saved using save() if they are created or updated with a new value for one of the fields
# however if you are mapping models instances to other model instances such as with array using keyword "ManyToMany" then u don't need to use "save()" to keep the changes