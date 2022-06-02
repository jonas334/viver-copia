from django.contrib import admin
from apps.usuario.models import Usuario, TokenEmail


# Register your models here.
admin.site.register(Usuario)
admin.site.register(TokenEmail)