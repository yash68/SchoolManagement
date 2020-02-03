from django.urls import path, include
from .views import *

urlpatterns = [
    path('', loginpage, name ='login'),
    path('dashboard/',dashboard, name = 'dashboard'),
    path('update/',updateTeacher,name="updateTeacher"),
    path('auth/',auth_view,name="auth"),
    path('addstudent/',addstudent, name='addstudent'),
    path('show/', showstudent, name= 'showstudent'),
    path('delete/<int:id>/', deletestudent, name= 'delete'),
    path('update/<int:id>/', updatestudent, name= 'update'),
    path('register/', registration, name = 'register')

]


