from django import forms
from django.forms import ModelForm

from catalog.models import ilaksa

class CreateFrom(ModelForm):
    name = forms.CharField(max_length=200, help_text="Краткое описание идеи")
    descr = forms.CharField(max_length=1000, help_text="Описание идеи подробнее", required=False)
    date_start = forms.DateField()

    STATUS_IDEA = (
        ('t', 'Реальна'),
        ('z', 'Забил хуй'),
    )

    status_idea = forms.ChoiceField(choices=STATUS_IDEA,
    help_text='Что с идеей Айлаксы сейчас')
    date_finish = forms.DateField(required=False)
    class Meta:
        model = ilaksa
        fields = ['name', 'descr', 'date_start', 'status_idea', 'date_finish']