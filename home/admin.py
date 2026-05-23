from django.contrib import admin
from .models import ContactSubmission, Certificate

admin.site.register(ContactSubmission)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'issuer')
