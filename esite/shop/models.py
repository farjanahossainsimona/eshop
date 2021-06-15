from django.db import models
from account.models import User
# from home.models import OFF_DAYS, YES_NO


SHOP_RATING = (
	(5, '5 Star'),
	(4, '4 Star'),
	(3, '3 Star'),
	(2, '2 Star'),
	(1, '1 Star'),
)


OFF_DAYS = (
	('friday', 'Friday'),
	('saturday', 'Saturday'),
	('sunday', 'Sunday'),
	('monday', 'Monday'),
	('tuesday', 'Tuesday'),
	('wednesday', 'Wednesday'),
	('thursday', 'Thursday'),
	('no_off', 'No Off Day'),
)


class Shop(models.Model):
	name = models.CharField(max_length=50)
	shopname = models.CharField(max_length=50)
	created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="shop owner")
	total_visited = models.IntegerField(blank=True, default=0)
	phone1 = models.CharField(max_length=20)
	phone2 = models.CharField(max_length=20)
	email = models.EmailField(max_length=50, null=True, blank=True)
	type = models.TextField(max_length=1000)
	delivery_status = models.CharField(max_length=50)
	district = models.CharField(max_length=64)
	location = models.TextField(max_length=200)
	off_day = models.CharField(max_length=100, default='friday', choices=OFF_DAYS)
	star = models.IntegerField(default=0, editable=False)
	# shop_active = models.CharField(max_length=1, default='0', choices=YES_NO)
	# shop_block = models.CharField(max_length=1, default='0', choices=YES_NO)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	notes = models.TextField(max_length=2000)
	deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.shopname
