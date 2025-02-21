from django.urls import path
from .views import get_predictions, pred , features

urlpatterns = [
    path('', pred, name='home'),
    path('features/' , features , name='features'),
    path('result', get_predictions, name='result'),
]
