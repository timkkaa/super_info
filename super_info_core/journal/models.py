from django.db import models
from ckeditor.fields import RichTextField



class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категория публикации'

class Hashtag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Хэштеги'
        verbose_name = 'Хэштег'

        def __str__(self):
            return self.title

class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hashteg = models.ManyToManyField(Hashtag)
    title = models.CharField(verbose_name='название', max_length=255)
    short_description = models.TextField(max_length=500)
    description = models.TextField()
    image = models.ImageField()

    created_te = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'


class PublicationComment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)



class AboutMe(models.Model):
    descrption = RichTextField(config_name='awesome_ckeditor')

