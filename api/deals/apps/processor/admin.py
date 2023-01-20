from django.contrib import admin
from django.contrib.auth.models import Group


from deals.apps.processor.models import Transaction, Item, Client


admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Client)
