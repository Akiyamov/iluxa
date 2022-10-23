from django import forms
from django.forms import ModelForm

from catalog.models import ilaksa

class CreateFrom(ModelForm):
    name = forms.CharField(max_length=200, label="Название")
    descr = forms.CharField(max_length=1000, required=False, label="Краткое описание идеи")
    date_start = forms.DateField(widget=forms.SelectDateWidget(), label="День начала")

    STATUS_IDEA = (
        ('t', 'Реальна'),
        ('z', 'Забил хуй'),
    )

    status_idea = forms.ChoiceField(choices=STATUS_IDEA,
    label="Статус идеи")
    date_finish = forms.DateField(required=False, widget=forms.SelectDateWidget(), label="Дата конца")
    class Meta:
        model = ilaksa
        fields = ['name', 'descr', 'date_start', 'status_idea', 'date_finish']
