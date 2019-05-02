from django.contrib import admin

from usuario.models import Ideas, Tablero, Estados_tablero, Estados_idea

admin.site.register(Ideas)
admin.site.register(Tablero)
admin.site.register(Estados_tablero)
admin.site.register(Estados_idea)
# Register your models here.
