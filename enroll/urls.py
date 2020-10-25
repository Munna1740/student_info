from django.urls import path
from . import views



urlpatterns = [
    path('', views.addAndShow, name="addandshow"),
    path('deletedata/<id>', views.delete_data, name="deletedata"),
    path('update/<id>', views.update_data, name="updatedata"),
]
