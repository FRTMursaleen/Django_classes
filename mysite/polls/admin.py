from django.contrib import admin
from .models import Accounts,Songs,Post,Todo
# Register your models here.

class AccountsData(admin.ModelAdmin):
    list_display = ["user","age", "name", "gender"]
    class Meta:
        model = Accounts


admin.site.register(Accounts,AccountsData)
admin.site.register(Songs)
admin.site.register(Post)
admin.site.register(Todo)