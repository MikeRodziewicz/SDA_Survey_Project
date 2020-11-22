from django.contrib import admin
from .models import TestModel, WisdomNote, NewsTags, NewsCategory, Formularz

admin.site.register(TestModel)
admin.site.register(WisdomNote)
admin.site.register(NewsTags)
admin.site.register(NewsCategory)
admin.site.register(Formularz)
