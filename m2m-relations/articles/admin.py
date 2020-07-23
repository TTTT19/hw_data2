from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Article_Tag, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data["is_main"]:
                main_tags_count += 1

            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

        if main_tags_count != 1:
            raise ValidationError('Определите один главный тег')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Article_Tag
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass