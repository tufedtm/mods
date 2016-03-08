from django.contrib import admin
from models import Magazine, Game, Patch


class MagazineAdmin(admin.ModelAdmin):
    list_display = ['title_display']
    readonly_fields = ['id', 'created', 'updated']

    fieldsets = (
        (None, {
            'fields': ('title', 'number', 'public_year', 'public_month', 'cover', (
                'id', 'created', 'updated'
            )),
        }),
    )

    def title_display(self, obj):
        return '%s %s' % (obj.get_title_display(), obj.number)


class GameAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'updated']


class PatchAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'created', 'updated']


admin.site.register(Magazine, MagazineAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Patch, PatchAdmin)
