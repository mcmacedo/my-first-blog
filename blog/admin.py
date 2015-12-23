from django.contrib import admin
from .models import Post
"""
	Torna o nosso Modelo 'Post' disponível 
	na página de Administração.
"""

admin.site.register(Post)
