from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import *
from stuff.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
# ----------------------------------------------------------------------------------------------------------------------------
class ProfileUser(models.Model):
    image = models.ImageField(upload_to='web_shop/users/%Y/%m/%d/')
    bio = models.CharField(max_length=500)

    def __str__(self):
        return str(self.bio)
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    phoneNumber = models.CharField(unique=True, max_length=11)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    profile = models.OneToOneField(ProfileUser,on_delete=models.SET_NULL,blank=True,null=True,related_name="user") 
    

    can_change_password = models.BooleanField(default=False)


    code = models.IntegerField(blank=True,null=True)


    wishlist = models.ManyToManyField(Product,blank=True,related_name ="wishlist")
    informing = models.ManyToManyField(Product,blank=True,related_name ="informing")



    USERNAME_FIELD = 'phoneNumber'
    objects = MyUserManager()

    def __str__(self):
        return str(self.phoneNumber) + " - " + str(self.full_name)

    # def full_name(self):
    #     return str(self.full_name) + " " + str(self.lastName)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# ----------------------------------------------------------------------------------------------------------------------------
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
    text = models.TextField()
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20,blank=True,null=True)
    current = models.BooleanField(default=False)



    def __str__(self):
        return str(self.user) + " - " + str(self.postal_code)

#----------------------------------------------------------------------------------------------------------------------------
from facades.utils import jalali_converter_with_hour
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=False)

    rating = models.FloatField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)

    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')


    def __str__(self):
        return f"{self.user.full_name}"

    def star_rating(self):
        return self.rating * 20

    def shamsi_date(self):
        return jalali_converter_with_hour(self.created) 
    
    def days_since_creation(self):
        now = timezone.now()
        created_naive = timezone.make_naive(self.created, timezone.get_default_timezone())
        created_aware = timezone.make_aware(created_naive, timezone.get_default_timezone())
        days = (now - created_aware).days
        return f"{days} روز پیش"
#----------------------------------------------------------------------------------------------------------------------------
class ProductComment(Comment):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user.full_name} - {self.product.name}"
#----------------------------------------------------------------------------------------------------------------------------
from blog.models import Post
class PostComment(Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user.full_name} - {self.post.title}"
#----------------------------------------------------------------------------------------------------------------------------
class WatchedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="wacthed")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.product.name} - {self.timestamp}"
#-----------------------------------------------------------------------------------
