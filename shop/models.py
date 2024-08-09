from django.db import models


# Create your models here.
class Product(models.Model):
    p_id = models.AutoField
    p_name = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    p_desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.p_name


class Contact(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name
