from django.db import models
from .category import Category
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    saleprice = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = RichTextUploadingField(default='SOME STRING')
    brand = RichTextUploadingField(default='SOME STRING')
    dimensions = models.CharField(max_length=50, default='SOME STRING')
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
