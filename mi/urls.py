from django.urls import path
from mi.views import *
app_name="Everything"
urlpatterns = [path("captain/",captain,name="captain"),
               path("vicecaptain/",vicecaptain,name="vicecaptain"),
    
]

