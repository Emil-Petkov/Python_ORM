from django.contrib import admin

from main_app.models import EventRegistration


# Register your models here.

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "event_name",
        "participant_name",
        "registration_date",
    )

    list_filter = (
        "event_name",
        "registration_date",
    )

    search_fields = (
        "event_name",
        "participant_name",
    )
