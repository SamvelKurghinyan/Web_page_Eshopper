from django.db import models

# Create your models here.

class HomeSliderActive(models.Model):
    title = models.CharField('HomeSliderActive title', max_length=30)
    name = models.CharField('HomeSliderActive name', max_length=50)
    about = models.TextField('HomeSliderActive about')
    img = models.ImageField('HomeSliderActive image', upload_to='media')
    logo = models.ImageField('HomeSliderActive logo', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'HomeSliderActive'
        verbose_name_plural = 'HomeSlidersActive'


class HomeSlider(models.Model):
    title = models.CharField('HomeSlider title', max_length=30)
    name = models.CharField('HomeSlider name', max_length=50)
    about = models.TextField('HomeSlider about')
    img = models.ImageField('HomeSlider image', upload_to='media')
    logo = models.ImageField('HomeSlider logo', upload_to='media')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'HomeSlider'
        verbose_name_plural = 'HomeSliders'


class Contact_Us(models.Model):
    name = models.CharField('Contact_Us name', max_length=30)
    email = models.EmailField('Contact_Us email')
    subject = models.CharField('Contact_Us subject', max_length=50)
    about = models.TextField('Contact_Us about')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Contact_Us'
        verbose_name_plural='Contacts_Us'


class Category(models.Model):

    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categ')
    name = models.CharField('Sub Category name', max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'