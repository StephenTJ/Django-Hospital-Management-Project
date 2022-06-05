from django.urls import path
from .views import About, Dashboard, Delete_Appointment, Home, Login, Logout_admin, View_Doctor, Delete_Doctor, Add_Doctor, View_Patient, Add_Patient, Delete_Patient, View_Appointment, Add_Appointment, Delete_Staff, Add_Staff, View_Staff, View_Prescription, Add_Prescription, Delete_Prescription

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)/', Delete_Doctor, name='delete_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)/', Delete_Patient, name='delete_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)/',
         Delete_Appointment, name='delete_appointment'),
    path('view_staff/', View_Staff, name='view_staff'),
    path('add_staff/', Add_Staff, name='add_staff'),
    path('delete_staff(?P<int:pid>)/', Delete_Staff, name='delete_staff'),
    path('view_prescription/', View_Prescription, name='view_prescription'),
    path('add_prescription/', Add_Prescription, name='add_prescription'),
    path('delete_prescription(?P<int:pid>)/',
         Delete_Prescription, name='delete_prescription'),
]
