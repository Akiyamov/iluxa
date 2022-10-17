from django.db import models

# Create your models here.

class ilaksa(models.Model):
    name = models.CharField(max_length=200, help_text="Краткое описание идеи")
    descr = models.TextField(max_length=1000, help_text="Описание идеи подробнее", blank=True)
    date_start = models.DateField()

    STATUS_IDEA = (
        ('t', 'Реальна'),
        ('z', 'Забил хуй'),
    )

    status_idea = models.CharField(max_length=1, choices=STATUS_IDEA, default='t',
    help_text='Что с идеей Айлаксы сейчас')
    date_finish = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["date_start"]

    def __str__(self):
        return self.name
    
    def Create(cls, name, descr, date_start, status_idea, date_finish):
        ilaksa = cls(name, descr, date_start, status_idea, date_finish)
        return ilaksa
