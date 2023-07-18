from django.contrib import admin

# Register your models here.

from .models import training, testing, traintemp, testtemp, val_auto, val_manual, val_ovr

admin.site.register(training)
admin.site.register(testing)
admin.site.register(traintemp)
admin.site.register(testtemp)
admin.site.register(val_manual)
admin.site.register(val_auto)
admin.site.register(val_ovr)
