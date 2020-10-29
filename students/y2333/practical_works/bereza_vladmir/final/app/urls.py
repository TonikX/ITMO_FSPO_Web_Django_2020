
from django.urls import path, include
from django.urls import reverse
from .views import *


urlpatterns = [
    path('base', base, name='base_url'),
    #path('singup2', signup2, name='signup2_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('summary', summary, name='summary_url'),
    path('vacancy', vacancy, name='vacancy_url'),
    path('signup_job_seeker', signup_job_seeker, name='signup_job_seeker_url'),
    path('signup_employer', signup_employer, name='signup_employer_url'),
    path('account/<int:user_id>/', account, name='account_url'),
    path('vacancy_add/<int:user_id>/', vacancy_add, name='vacancy_add_url'),
    path('summary_add/<int:user_id>/', summary_add, name='summary_add_url'),
    path('summary_delete/<int:summary_id>/', summary_delete, name='summary_delete_url'),
    path('vacancy_delete/<int:vacancy_id>/', vacancy_delete, name='vacancy_delete_url'),
    path('response/<int:vacancy_id>/<int:user_id>/', response, name='response_url'),
 ]
