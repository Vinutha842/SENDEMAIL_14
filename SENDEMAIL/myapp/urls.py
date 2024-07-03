from django.urls import path
from.import views

urlpatterns=[
    path('contact/',views.contact_view,name='contact_client'),
    path('email_success/',views.email_success,name='email.success'),
]