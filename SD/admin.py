from .models import Payment, Patient, Doctor, Procedur, Coworker
from django.contrib import admin
from django.utils.html import format_html

@admin.register(Coworker)
class CoworkerAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = (
                    'surname',
                    'first_name',
                    'middle_name',
                    'phone',
                    'department',
                    'email',
                    'birthday',
                    'comment',
                    'date_created',
                    'status',
                    '_',
                    )
    ordering = ('-date_created',)
    search_fields = ('first_name', 'middle_name', 'surname', 'phone', 'status', 'department', 'email', 'comment')
    list_per_page = 20

    # Функция для изменения Иконки
    def _(self, obj):
        if obj.status == 'Запрос утвержден':
            return True
        elif obj.status == 'На рассмотрении':
            return None
        else:
            return False
    _.boolean = True

    # Функция для окрашивания текста
    def status(self, obj):
        if obj.status == 'Запрос утвержден':
            color = '#28a745'
        elif obj.status == 'На рассмотрении':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.status))
    status.allow_tags =True

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'FIO',
        'phone',
        'percent',
        'department',
        'email',
        'birthday',
        'date_created',
        'date_modified',
    )
    list_filter = ('date_created',)
    search_fields = ('patient', 'doctor', 'payment_method', 'evening_shift', 'date_created', 'date_modified')
    ordering = ('-date_created',)
    list_per_page = 20

@admin.register(Procedur)
class ProcedurAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'price',
                    'category',
                    'description',
                    'date_created',
                    'date_modified',
                    )
    list_filter = ('date_created',)
    search_fields = ('surname', 'phone', 'iin', 'note')
    ordering = ('-date_created',)
    list_per_page = 50

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'income',
        'payment_method',
        'technical_cost',
        'evening_shift',
        'doctor',
        'date_created',
        'date_modified',
        )
    list_filter = ('date_created',)
    search_fields = ('patient', 'doctor', 'payment_method', 'evening_shift', 'date_created', 'date_modified')
    ordering = ('-date_created',)
    list_per_page = 20

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'surname',
                    'middle_name',
                    'phone', 'iin',
                    'gender', 'age',
                    'note',
                    'date_modified',
                    )
    list_filter = ('date_created',)
    search_fields = ('surname', 'phone', 'iin', 'note')
    ordering = ('-date_created',)
    list_per_page = 50
