from django.urls import path
from .views import home, workout_plans, subscribe, rate_workout_plan

urlpatterns = [
    path('', home, name='home'),
    path('workout-plans/', workout_plans, name='workout_plans'),
    path('subscribe/<int:plan_id>/', subscribe, name='subscribe'),
    path('rate/<int:plan_id>/', rate_workout_plan, name='rate_workout_plan'),
]
