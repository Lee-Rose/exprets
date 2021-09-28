from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.lastname}'

class Article(models.Model):
    title = models.CharField(max_length=50)
    anons = models.CharField(max_length=500)
    director = models.CharField(max_length=30)
    year_of_release = models.IntegerField(default=2000)
    actors = models.ManyToManyField(Actor)
    thumb = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New film'
        verbose_name_plural ='Films'


class Person(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

class Review(models.Model):
    film = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Person,on_delete=models.CASCADE)
    datePublished = models.DateField()
    reviewBody = models.TextField()

