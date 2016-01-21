from django.contrib import admin
from .models import Blog
from .models import Post
from .models import Media
from .models import Tag

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(Tag)
# Register your models here.
