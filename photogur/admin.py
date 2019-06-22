from django.contrib import admin
from photogur.models import Picture, Comment

# registering Picture with the admin back-end
admin.site.register(Picture)
# registering Comment with the admin back-end
admin.site.register(Comment)
