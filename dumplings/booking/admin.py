from django.contrib import admin

from booking.models import (
    BookingModel,
    ListBooing,
)

from market.models import (
    Adress
)

# class ListBookingAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "adress":
#             # Получите выбранный объект Siti из формы
#             selected_siti = request.POST.get('siti')  # Проверьте, какое поле выбрано в вашей форме

#             # Установите ограничение выбора для поля adress на Adress, связанный с выбранным Siti
#             kwargs["queryset"] = Adress.objects.filter(siti_id=selected_siti)

#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

# admin.site.register(ListBooing, ListBookingAdmin)


admin.site.register(ListBooing)
admin.site.register(BookingModel)