from django import forms
from django.db.models import Q
from django_filters import FilterSet, filters
from .models import Sighting
from django.contrib.auth.models import User


class MultiOrderFilterSet(FilterSet):
    order_by_field = 'order_by'

    def get_order_by(self, order_choice):
        res = super(MultiOrderFilterSet, self).get_order_by(order_choice)
        order_bys = []
        for f in res:
            direction = ''
            if f.startswith('-'):
                direction = '-'
                f = f.lstrip('-')
            order_by = [direction+o.strip() for o in f.split(',')]
            order_bys.extend(order_by)
        return order_bys


class MySightingFilter(MultiOrderFilterSet):
    class Meta:
        model = Sighting
        fields = []
        order_by = ['make', '-make', 'model', '-model', 'year', '-year',
                    'frame_number', '-frame_number', 'engine_number',
                    '-engine_number', ]
