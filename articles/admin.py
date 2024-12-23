from django.contrib import admin

from . import models

admin.site.register(models.Article)
admin.site.register(models.Comment)

class CommentInLine(admin.TabularInline):
	model = models.Comment

class ArticleAdmin(admin.ModelAdmin):
	inlines = [ CommentInLine, ]
# Register your models here.
