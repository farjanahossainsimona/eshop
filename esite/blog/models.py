from django.db import models
import os, uuid


def blog_data_path(instance, file_name):
	f_name, file_extension = os.path.splitext(file_name)
	file_name = str(uuid.uuid4()) + '_' + str(f_name) + str(file_extension)
	# file will be uploaded to MEDIA_ROOT/shop/<filename>
	return 'blog/{0}'.format(file_name)


class Blog(models.Model):
    heading = models.CharField(max_length=1500)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to=blog_data_path, null=True, blank=True)
    author = models.CharField(max_length=50)
    publish_date = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    tag = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=True)
    deleted = models.BooleanField(default=False, blank=True)