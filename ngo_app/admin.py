from django.contrib import admin
from .models import Contact,Feedback,User,Campaign,Service,Donation
class Contact_admin(admin.ModelAdmin):
    list_display=["name","email","phone","comment","date"]
class Feedback_admin(admin.ModelAdmin):
    list_display=["name","email","rating","remark","date"]





#Campaign
admin.site.register(Contact,Contact_admin)
admin.site.register(Feedback,Feedback_admin)
admin.site.register(User)
admin.site.register(Campaign)
admin.site.register(Donation)


admin.site.site_header="NGO Admin"
admin.site.site_title="NGO by Ritesh Admin Portal"
admin.site.index_title="NGO "
