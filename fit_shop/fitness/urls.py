from django.urls import path
from .views import home, workout_plans, subscribe, subscribe_free_trial, rate_workout_plan

urlpatterns = [
    path('', home, name='home'),
    path('workout-plans/', workout_plans, name='workout_plans'),
    path('subscribe/<int:plan_id>/', subscribe, name='subscribe'),
    path('rate/<int:plan_id>/', rate_workout_plan, name='rate_workout_plan'),
    path('subscribe-free-trial/', subscribe_free_trial,
         name='subscribe_free_trial'),
]
