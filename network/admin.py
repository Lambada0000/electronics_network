from django.contrib import admin
from .models import NetworkNode, Product


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "city", "debt", "created_at")
    list_filter = ("city",)
    search_fields = ("name",)
    actions = ["clear_debt"]

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
    clear_debt.short_description = "Очистить задолженность у выбранных объектов"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date", "network_node")