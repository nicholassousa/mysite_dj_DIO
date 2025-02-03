from django.contrib import admin
from .models import Choice, Question


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


# Register your models here.
