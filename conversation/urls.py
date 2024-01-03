from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/',views.detail, name='detail'),
    path('detail_mini/<int:pk>/',views.detail_mini, name='detail_mini'),
    path('new/<int:item_pk>/', views.new_conversation, name='new')
]