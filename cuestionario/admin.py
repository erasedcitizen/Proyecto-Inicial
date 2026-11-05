from django.contrib import admin
from .models import Universidad, Conflicto, Subconflicto, Orientacion

admin.site.register(Universidad)
admin.site.register(Conflicto)
admin.site.register(Subconflicto)
admin.site.register(Orientacion)