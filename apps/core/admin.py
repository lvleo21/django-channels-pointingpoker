from django.contrib import admin
from .models import (
    PointingPoker,
    Session,
    SessionUser,
    Estimate,
)
from apps.core import inlines


@admin.register(PointingPoker)
class PointingPokerAdmin(admin.ModelAdmin):
    list_display = ["session", "description"]
    list_filter = ["session"]
    inlines = [
        inlines.PointValueInline,
    ]


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ["description", "status", "allow_observers", "allow_participants_reset_votes"]
    list_filter = ["status"]


@admin.register(SessionUser)
class SessionUserAdmin(admin.ModelAdmin):
    list_display = ["name", "session", "role",]
    list_filter = ["role"]


@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    list_display = ["session", "score", "is_closed",]
    list_filter = ["session"]
    inlines = [
        inlines.UserEstimateInline,
    ]
    readonly_fields = ["score", "start_at", "close_at"]