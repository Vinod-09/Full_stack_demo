from django.urls import path
from . import views

urlpatterns = [
    path('',views.front_end, name='front_end'),
    path('mobile/',views.get_all_data,name='all-data'),
    path('mobile/<int:mobile_id>/',views.get_data_byID, name='data-id'),
    path('mobile/add/',views.add_mobile,name='add-mobile'),
    path('mobile/<int:mobile_id>/add/',views.add_new_features,name='new-feature'),
    path('mobile/<int:mobile_id>/update/',views.update_data,name='update-data'),
    path('mobile/<int:mobile_id>/delete/',views.delete_data,name='delete-data')
]