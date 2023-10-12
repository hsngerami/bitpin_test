from rest_framework.urls import path

from api.routes.rates import CreateRateView

endpoints = [
    path('', CreateRateView.as_view(), name="rate_post"),
]
