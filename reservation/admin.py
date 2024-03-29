from django.contrib import admin

from reservation.models import Reservation

class reservationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        return True

admin.site.register(Reservation, reservationAdmin)
