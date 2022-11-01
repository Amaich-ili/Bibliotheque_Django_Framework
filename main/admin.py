from django.contrib import admin
from .models import Categories
from .models import Liste_livre
from .models import Lecteur

admin.site.register(Categories)
admin.site.register(Liste_livre)
admin.site.register(Lecteur)
