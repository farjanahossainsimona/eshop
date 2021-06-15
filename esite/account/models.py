from django.db import models
# from shop.models import Shop
# from home.models import Product
import os

def profile_pic_path(instance, file_name):
	f_name, file_extension = os.path.splitext(file_name)
	file_name = str(instance.username) + str(file_extension)
	# file will be uploaded to MEDIA_ROOT/user/<user_id>/<filename>
	return 'user/{0}/{1}'.format(instance.id, file_name)


GENDER = (
	('male', 'Male'),
	('female', 'Female'),
)

DISTRICT = (
	('manikganj', 'Manikganj'),
	('dhaka', 'Dhaka'),
	('faridpur', 'Faridpur'),
)

USER_ROLE_LIST = (
	('admin', 'Admin'),
	('editor', 'Editor'),
	('moderator', 'Moderator'),
)

class User(models.Model):
	username = models.CharField(max_length=50)
	full_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50, null=True, blank=True)
	email_verify = models.CharField(max_length=10, default='0')
	phone = models.CharField(max_length=15, unique=True)
	phone_verify = models.CharField(max_length=10, default='0')
	gender = models.CharField(max_length=100, null=True, blank=True, choices=GENDER)
	password = models.CharField(max_length=264)
	password_recovery = models.CharField(max_length=10, default='0')
	last_login = models.DateTimeField(null=True, blank=True)
	profile_pic = models.ImageField(upload_to=profile_pic_path, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	district = models.CharField(max_length=64, null=True, blank=True, choices=DISTRICT)
	account_active = models.CharField(max_length=1, default='0')
	account_block = models.CharField(max_length=1, default='0')
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.username

	def filename(self):
		return os.path.basename(self.profile_pic.name)

	class Meta:
		verbose_name_plural = 'users'


# class UserRole(models.Model):
# 	user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="user id")
# 	role_name = models.CharField(max_length=50, choices=USER_ROLE_LIST)
# 	shop_id = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name="shop by")

# 	def __str__(self):
# 		shop_name = self.shop_id.shopname
# 		user_name = self.user_id.username
# 		result = user_name + "_" + shop_name + "(" + self.role_name + ")"
# 		return self.role_name



# class UsersProductWishlist(models.Model):
# 	product_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="product name")
# 	wishlist_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="user by name")
# 	created_at = models.DateTimeField(auto_now_add=True, editable=False)
# 	updated_at = models.DateTimeField(auto_now=True, editable=False)
# 	deleted = models.BooleanField(default=False)

# 	def __str__(self):
# 		return str(self.product_id)