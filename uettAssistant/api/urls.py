from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',views.getRoutes,name='routes'),
    path('departments/',views.getDepartment,name='departments'),
    # path('task/<int:id>',views.getTask,name='getTAsk'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
