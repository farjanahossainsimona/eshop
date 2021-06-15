from django.db import models
from account.models import User
from shop.models import Shop
import os


YES_NO = (
	('1', 'Yes'),
	('0', 'No'),
)


PRODUCT_SIZE = (
	('zero', 'ZERO'),
	('xs', 'XS'),
	('s', 'S'),
	('m', 'M'),
	('l', 'L'),
	('xl', 'XL'),
	('xxl', 'XXL'),
)

PRODUCT_STAR = (
	(5, '5 Star'),
	(4, '4 Star'),
	(3, '3 Star'),
	(2, '2 Star'),
	(1, '1 Star'),
)


class Color(models.Model):
	bengali_name = models.CharField(max_length=64)
	english_name = models.CharField(max_length=64)

	def __str__(self):
		return self.english_name


class Category(models.Model):
	bengali_name = models.CharField(max_length=150)
	english_name = models.CharField(max_length=150)

	def __str__(self):
		return self.english_name


class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="category")
	bengali_name = models.CharField(max_length=150)
	english_name = models.CharField(max_length=150)

	def __str__(self):
		return self.english_name


class SubSubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="category")
	sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name="sub category",)
	bengali_name = models.CharField(max_length=150)
	english_name = models.CharField(max_length=150)

	def __str__(self):
		return self.english_name


class Product(models.Model):
	bengali_name = models.CharField(max_length=150)
	english_name = models.CharField(max_length=150)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="product category")
	sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name="sub category", blank=True, null=True)
	sub_sub_category = models.ForeignKey(SubSubCategory, on_delete=models.PROTECT, verbose_name="sub sub category", blank=True, null=True)
	color = models.ForeignKey(Color, on_delete=models.PROTECT, verbose_name="product color", blank=True, null=True)
	code = models.CharField(max_length=50, blank=True, null=True)
	description = models.TextField(max_length=2000, blank=True, null=True)
	stock = models.IntegerField(default=0)
	total_sale = models.IntegerField(default=0)
	purchase_price = models.IntegerField(blank=True, default=0)
	sale_price = models.IntegerField(default=0)
	discount = models.IntegerField(default=0, blank=True)
	sizes = models.CharField(max_length=50, blank=True, null=True, choices=PRODUCT_SIZE)
	notes = models.TextField(max_length=2000, blank=True, null=True)
	created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="product create by", blank=True)
	shop_by = models.ForeignKey(Shop, on_delete=models.PROTECT, verbose_name="product shop by", blank=True)
	status = models.CharField(max_length=1, default='1', choices=YES_NO)
	rating = models.IntegerField(editable=False, default=0, blank=True)
	total_visited = models.IntegerField(editable=False, default=0, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
	updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)
	deleted = models.BooleanField(default=False, blank=True)

	def __str__(self):
		english_name = self.english_name
		return str(english_name)


def product_data_path(instance, file_name):
	f_name, file_extension = os.path.splitext(file_name)
	file_name = str(instance.product_id) + '_' + str(instance.product_id.shop_by.id) + str(file_extension)
	# file will be uploaded to MEDIA_ROOT/shop/<shop_id>/<filename>
	return 'shop/{0}/{1}'.format(instance.product_id.shop_by.id, file_name)


class ProductPic(models.Model):
	product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="product id", blank=True)
	pic_name = models.ImageField(upload_to=product_data_path)
	created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)

	def __str__(self):
		pic_name = self.pic_name
		return str(pic_name)

	def filename(self):
		return os.path.basename(self.pic_name.name)


class ProductReview(models.Model):
	product_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="product name")
	title = models.CharField(max_length=50)
	details = models.TextField(max_length=2000)
	star = models.SmallIntegerField(default=5, choices=PRODUCT_STAR)
	review_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="reviewer name")
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class ProductReviewComment(models.Model):
	review_title = models.ForeignKey(ProductReview, on_delete=models.PROTECT, verbose_name="review title")
	details = models.TextField(max_length=2000)
	star = models.SmallIntegerField(default=False)
	commented_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="commenter name")
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.review_title
