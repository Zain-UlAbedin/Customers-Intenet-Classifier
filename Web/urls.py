from django.urls import path
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home, name='Web_home'),
    path('About_us/', views.About, name='Web_About'),
    path('Contact_us/', views.Contact, name='Web_Contact'),
    path('Create_User', views.Create_User, name='Web_User'),
    path('Login/Log', views.Log_User, name='Web_LogUser'),
    #path('Login/', views.Log_in, name='Web_LogIn'),
    url(r'Login/', views.Log_in, name='Web_LogIn'),
    path('User_DashBoard/', views.User_DashBoard, name='Web/DashBoard'),
    url(r'logout/$', views.logout),
    url(r'Upload', views.File_Upload),
    url(r'media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'Insights/(?P<Path>.*)/$', views.Insight, name="Web_Insights"),
    path('Statistics/', views.Statistics, name="Web_Statistic"),
    #url(r'Barchart$', views.Bar_Chart, name="Web_"),
    url(r'Donutchart/(?P<Path>.*)/$', views.Donut_Chart, name="Web_donutchart"),
    url(r'Barchart/(?P<Path>.*)/$', views.Bar_Chart, name="Web_barchart"),
    url(r'Treemap/(?P<Path>.*)/$', views.TreeMap, name="Web_Treemap"),
    url(r'Wordcloud/(?P<Path>.*)/$', views.Word_Cloud, name="Web_Wordcloud"),

    #path('Donutchart/', views.Donut_Chart, name="Web_donustchart"),
    #path('Barchart/', views.Bar_Chart, name="Web_barchart")

    #path('Insights/<Path>', views.Insights, name='Web_Insights'),

]
