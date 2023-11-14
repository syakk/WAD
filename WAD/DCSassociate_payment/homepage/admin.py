from django.contrib import admin
from .models import Associate, Student, Payment, Affair
# Register your models here.
admin.site.register(Associate)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Affair)