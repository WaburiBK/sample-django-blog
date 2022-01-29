from django.contrib import admin

# modifying poll app in admin page
# telling admin that Question objects have admin interface
from .models import Question

admin.site.register(Question)