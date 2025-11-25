from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"), # Empty path : /challenges/
    path("<int:month>", views.monthly_challenges_response_number),
    # path("<str:month>", views.monthly_challenges),
    path("<str:month>", views.monthly_challenges_dict_view, name="month-challenge"),
]
