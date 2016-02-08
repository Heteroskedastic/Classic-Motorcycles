from django.contrib import admin
from .models import Search, UserSearchHistory

class UserSearchHistoryAdmin(admin.ModelAdmin):
	list_display = ('search','pub_date', 'ip_address')


admin.site.register(Search)
admin.site.register(UserSearchHistory, UserSearchHistoryAdmin)
