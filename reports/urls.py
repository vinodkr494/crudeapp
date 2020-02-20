from django.urls import path
from . views import report_view,delete_view,ReportUpdateView,HomeView,SelectView

app_name='reports'

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('reports/',SelectView.as_view(),name='select_view'),
    path('reports/<str:productionline>/',report_view,name='report_view'),
    path('reports/delete/<pk>',delete_view,name='delete_view'),
    path('reports/<str:productionline>/<pk>/update/',ReportUpdateView.as_view(),name='update-view')
]
