from django.conf.urls import url

from . import views

urlpatterns = [
		# Students urls
		url(r'^$', views.students_list, name='home'),
		url(r'^students/add$', views.students_add, name='students_add'),
		url(r'^students/(?P<sid>\d+)/edit/$', views.students_edit, name='students_edit'),
		url(r'^students/(?P<sid>\d+)/delete/$', views.students_edit, name='students_delete'),

		# Groups urls
		url(r'^groups/$', views.groups_list, name='groups'),
		url(r'^groups/add/$', views.groups_add, name='groups_add'),
		url(r'^groups/(?P<gid>\d+)/edit/$', views.groups_edit, name='groups_edit'),
		url(r'^groups/(?P<gid>\d+)/delete/$', views.groups_delete, name='groups_delete'),
		
]
