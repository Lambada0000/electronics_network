from django.contrib import admin
from .models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        updated_count = queryset.update(debt=0)
        self.message_user(request, f'{updated_count} объектов обновлено.')
    clear_debt.short_description = "Очистить задолженность перед поставщиком"
