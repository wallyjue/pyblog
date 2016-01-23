from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField(blank=True)
	domain = models.CharField(max_length=100)
	photo = models.URLField(blank=True)
	public = models.BooleanField(blank=True)
	owner = models.ForeignKey(User)
	def __str__(self):
		return u"%s" % (self.title)

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(Blog)

	def __str__(self):
		return u"%s" % (self.title)

class Media(models.Model):
	mediafile = models.URLField(blank=True)
	post = models.ForeignKey(Post)
	def __str__(self):
		return u"%s" % (self.mediafile)

class Tag(models.Model):
	post = models.ForeignKey(Post,null=True, blank=True, default = None)
	tag = models.CharField(max_length=100)
	def __str__(self):
		return u"%s" % (self.tag)

class Category(models.Model):
	post = models.ForeignKey(Post,null=True, blank=True, default = None)
	name = models.CharField(max_length=100)
	def __str__(self):
		return u"%s" % (self.name)