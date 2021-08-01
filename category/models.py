from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True,max_length=300)
    description = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to = 'photos/categories',blank=True)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'





    def __str__(self):
        return self.Category_name

