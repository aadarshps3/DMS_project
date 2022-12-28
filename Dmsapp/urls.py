from  django.urls import path

from Dmsapp import views

urlpatterns = [
    path('student_register',views.student_register,name='student_register'),
    path('',views.admin_home,name='admin_home'),
    path('student_view',views.student_view,name='student_view'),
    path('Notification_add',views.Notification_add,name='Notification_add'),
    path('Notification_view',views.Notification_view,name='Notification_view'),
    path('add_attendance',views.add_attendance,name='add_attendance'),
    path('mark/<int:id>/',views.mark,name='mark'),
    path('view_attendance',views.view_attendance,name='view_attendance'),
    path('add_internal_mark',views.add_internal_mark,name='add_internal_mark'),
    path('view_internal_mark',views.view_internal_mark,name='view_internal_mark'),
    path('update_internal/<int:id>/',views.update_internal,name='update_internal'),
    path('del_internal/<int:id>/',views.del_internal,name='del_internal'),
]