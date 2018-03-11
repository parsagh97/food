from django.db import models

# Create your models here.
class User(models.Model):
    male = 1
    female = 2
    NonBinarySex=3
    sex = ((male,'male') ,(female ,'female') ,(NonBinarySex ,'nbs'))
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length= 15,unique=True,primary_key=True)
    gender = models.IntegerField(choices=sex)
    profile = models.ImageField(upload_to='profile_images' ,blank=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=15 ,blank=True)

    def __str__(self):
        return '{}'.format(self.user_name)

class recipe(models.Model):
    food_id = models.CharField(max_length=5 ,unique=True,primary_key=True)
    food_title = models.CharField(max_length=20)
    food_image = models.ImageField(upload_to='recipe_images', blank=True)
    def __str__(self):
        return '{}-{}'.format(self.food_id ,self.food_title)

class user_recipe(models.Model):
    food_id = models.ForeignKey(recipe ,on_delete=models.CASCADE)
    user_id =models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.food_id ,self.user_id)

class tag(models.Model):
    tag_id = models.CharField(max_length=5 ,unique=True ,primary_key=True)
    tag_title = models.CharField(max_length=10)

    def __str__(self):
        return '{}-{}'.format(self.tag_title ,self.tag_id)

class recipe_tag(models.Model):
    tag_id = models.ForeignKey(tag ,on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(recipe ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.tag_id ,self.recipe_id)

class peymane(models.Model):#پیمانه
    title = models.CharField(max_length=20)
    peymane_id = models.CharField(max_length=5 ,unique=True ,primary_key=True)

    def __str__(self):
        return '{}-{}'.format(self.title ,self.peymane_id)

class ingredient(models.Model):
    ingr_id = models.CharField(max_length=5 ,primary_key=True)
    ingr_title = models.CharField(max_length=30)

    def __str__(self):
        return '{}-{}'.format(self.ingr_id ,self.ingr_title)

class recipe_ingredient(models.Model):
    recipe = models.ForeignKey(recipe ,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(ingredient ,on_delete=models.CASCADE)
    peymane_id = models.ForeignKey(peymane ,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return '{}-{}'.format(self.ingredient ,self.recipe)
