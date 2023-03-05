from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES=(
('Andaman & Nicobar Islands ','Andaman & Nicobar Islands'),    
('Andhra Pradesh ','Andhra Pradesh '),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chandigarh','Chandigarh'),
('Chattisgarh','Chattisgarh'),
('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
('Daman and Diu','Daman and Diu'),
('Delhi','Delhi'),
('Goa','Goa'),
('Gujrat','Gujrat'),
('Haryane','Haryane'),
('Himachal Pradesh','Himachal Pradesh'),
('Jammu & Kashmir','Jammu & Kashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Keraka','Keraka'),
('Lakshadweep','Lakshadweep'),
('Madhya pradesh','Madhya pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisa','Odisa'),
('Puducharry','Puducharry'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttarakhand','Uttarakhand'),
('Uttar Pradesh','Uttar Pradesh'),
('West Bengal','West Bengal'),
)


# Create your models here.
CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','milk'),
    ('LS','Lassi'),
    ('MS','milkshake'),
    ('PN','paneer'),
    ('GH','Ghee'),
    ('CZ','Cheeae'),
    ('IC','Ice-Cremas'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    conposition = models.TextField(default='')
    prodapp = models.TextField(default='')
    categoty = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')
    def  __str__(self):
        return self.title
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    moblie=models.IntegerField()
    zipcode=models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self) :
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)









































# @property
# def total_cost(self): 
#       return self.quantite * self.product.discounted_price