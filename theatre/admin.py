from django.contrib import admin
from .models import Theatre, Show
from datetime import timedelta


class AddTheatre(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

admin.site.register(Theatre, AddTheatre)

class AddShow(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "theatre":
            kwargs["queryset"] = Theatre.objects.filter(admin_id=request.user)
        return super(AddShow, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):

        data = obj.date
        date_list=[]

        for i in range(1,7):
            date_list.append(data+timedelta(days=i))

        insert_list=[]
        for i in date_list:
            insert_list.append(Show(movie=obj.movie, theatre=obj.theatre, screen=obj.screen, date=i, time=obj.time))
        
        Show.objects.bulk_create(insert_list)
        obj.save()

admin.site.register(Show, AddShow)
