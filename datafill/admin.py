from django.contrib import admin
from models import Magazine, Game, Patch


class ReadOnlyFields(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'updated']


class MagazineAdmin(ReadOnlyFields):
    list_display = ['title_display']

    def title_display(self, obj):
        return '%s %s' % (obj.get_title_display(), obj.number)


admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Game, ReadOnlyFields)
admin.site.register(Patch, ReadOnlyFields)
