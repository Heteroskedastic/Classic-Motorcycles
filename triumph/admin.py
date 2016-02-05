from django.contrib import admin
from .models import Triumph, UserSearchHistory

class UserSearchHistoryAdmin(admin.ModelAdmin):
	list_display = ('term', 'result','pub_date', 'ip_address')


admin.site.register(Triumph)
admin.site.register(UserSearchHistory, UserSearchHistoryAdmin)
