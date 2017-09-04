from datetime import date
from django import forms
from django_filters import FilterSet, filters
from .models import Sighting


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


year_choices = [(None, '')] + \
    [(i, i) for i in range(1950, date.today().year + 1)]


class AllSightingFilter(MultiOrderFilterSet):
    year = filters.ChoiceFilter(
        required=False, choices=year_choices,
        widget=forms.Select(attrs={
            'style': 'width: 200px',
            'data-placeholder': 'Filter by Year',
            'class': 'chosen-select-deselect'}))
    make = filters.CharFilter(
        required=False, widget=forms.TextInput(attrs={
            'style': 'width: 200px; height: 28px;',
            'placeholder': 'Filter by Make',
            'class': ''}))
    model = filters.CharFilter(
        required=False, widget=forms.TextInput(attrs={
            'style': 'width: 200px; height: 28px;',
            'placeholder': 'Filter by Model',
            'class': ''}))

    class Meta:
        model = Sighting
        fields = ['make', 'model', 'year', ]

        order_by = ['make', '-make', 'model', '-model', 'year', '-year',
                    'frame_number', '-frame_number', 'engine_number',
                    '-engine_number', ]
