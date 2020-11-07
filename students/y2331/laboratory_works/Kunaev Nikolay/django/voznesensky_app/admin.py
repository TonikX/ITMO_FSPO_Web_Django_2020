from django.contrib import admin
from voznesensky_app.models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ("passport_id",
                    "full_name",
                    "birth_date",
                    "address_registration",
                    "address_residence",
                    "occupation",
                    "phones",
                    "gender",
                    "birth_place",
                    "discovery_info",
                    "email",
                    "comment",
                    "comment_addition",
                    "balance",
                    "permanent_discount",
                    "is_archived",
                    "archived_reason",
                    )


class DiscountCardAdmin(admin.ModelAdmin):
    list_display = ("percent", "client")


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("change", "date_time", "comment", "client")


class ItemAdmin(admin.ModelAdmin):
    list_display = ("qty", "name", "price", "group")


class SoldItemAdmin(admin.ModelAdmin):
    list_display = ("item", "price_actual", "client", "date", "isDiscountCardUsed")


class VisitAdmin(admin.ModelAdmin):
    list_display = ("date", "isFirst", "reason", "comment", "client", "isDiscountCardUsed", "status")


admin.site.register(Client, ClientAdmin)
admin.site.register(DiscountCard, DiscountCardAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(SoldItem, SoldItemAdmin)
admin.site.register(Visit, VisitAdmin)
