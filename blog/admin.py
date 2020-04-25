from django.contrib import admin

#importuje model do bazy
from .models import Post

admin.site.register(Post)
# Register your models here.
