from django.urls import path, include
from . import views

urlpatterns = [

    # Home page
    path('', views.home, name='home'),
    path('select2/', include('django_select2.urls')),

    # 404 Next Update
    path('next_update', views.next_update, name='next_update'),

    # dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    #CRUD Coworker:
    path('coworker_create', views.coworker_create, name='coworker_create'),

    #CRUD Doctor:
    path('doctor_create', views.doctor_create, name='doctor_create'),

    #CRUD Patient:
    path('patient_create', views.patient_create, name='patient_create'),

    # CRUD Procedurs:
    path('procedur_create', views.procedur_create, name='procedur_create'),

    #CRUD Payment:
    path('payment_create', views.payment_create, name='payment_create'),


]


"""
    path('dashboard', views.dashboard, name='dashboard'),

    path('patient_personal_page/<str:pk>/', views.patient_personal_page, name="patient_personal_page"),
    path('patient/<str:patient_id>/', views.patient, name="patient"),
    path('patient_update', views.patient_update, name="patient_update"),
    path('patient_delete/<str:pk>/', views.patient_delete, name="patient_delete"),
    path('patients_database/', views.patients_database, name="patients_database"),

    # CRUD Doctors:
    path('doctor_personal_page/<str:pk>/', views.doctor_personal_page, name="doctor_personal_page"),
    path('doctor/<str:doctor_id>/', views.doctor, name="doctor"),
    path('doctor_update', views.doctor_update, name="doctor_update"),
    path('doctor_delete/<str:pk>/', views.doctor_delete, name="doctor_delete"),
    path('doctors_database/', views.doctors_database, name="doctors_database"),

    # CRUD Payments:
    path('payment_create', views.payment_create, name="payment_create"),
    path('payment/<str:payment_id>/', views.payment, name="payment"),
    path('payment_update', views.payment_update, name="payment_update"),
    path('payment_delete/<str:pk>/', views.payment_delete, name="payment_delete"),
    path('payments_database/', views.payments_database, name="payments_database"),

    path('procedur_personal_page/<str:pk>/', views.procedur_personal_page, name="procedur"),
    path('procedur_update/<str:pk>/', views.procedur_update, name="procedur_update"),
    path('procedur_delete/<str:pk>/', views.procedur_delete, name="procedur_delete"),
    path('procedurs_database/', views.procedurs_database, name="procedurs_database"),
]
"""
