from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs')
    category = models.ForeignKey(CategoryModel, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'