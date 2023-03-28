from django.contrib import admin
from apps.core.models import (
    PointValue, UserEstimate
)


class PointValueInline(admin.StackedInline):
    model = PointValue 
    extra=0
    min_num=1
    fieldsets = (
        (None, {'fields': (('label', 'value',),)}),
    )


class UserEstimateInline(admin.StackedInline):
    model = UserEstimate 
    extra=0
    min_num=1
    fieldsets = (
        (None, {'fields': (('point_value', 'session_user',),)}),
    )
