from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add_stu',views.add_student,name='add_student'),
    path('stu_detail',views.student_details,name='student_detail'),
    path('spe_detail/<int:pk>',views.spe_detail,name='spe_detail'),
    path('edit_stu/<int:pk>',views.edit_student,name='edit_student'),
    path('delete_stu/<int:pk>',views.delete_student,name='delete_student'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('action_con',views.contact_action,name='contact_action'),
]