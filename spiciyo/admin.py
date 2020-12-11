from django.contrib import admin
from .models import cards, slider_card, call_request, newsletter
# Register your models here.

admin.site.register(cards)
admin.site.register(slider_card)
admin.site.register(call_request)
admin.site.register(newsletter)
