from django.shortcuts import render
from .models import WorkoutPlan, Subscription, Rating


def home(request):
    free_trial_plan = WorkoutPlan.objects.get(title='Free Trial')
    premium_plan = WorkoutPlan.objects.get(title='Premium Plan')
    return render(request, 'fitness/home.html', {'free_trial_plan': free_trial_plan, 'premium_plan': premium_plan})


def workout_plans(request):
    plans = WorkoutPlan.objects.all()
    return render(request, 'fitness/workout_plan_list.html', {'plans': plans})


def subscribe(request, plan_id):
    if request.user.is_authenticated:
        plan = WorkoutPlan.objects.get(id=plan_id)
        Subscription.objects.create(user=request.user, workout_plan=plan)
        return render(request, 'fitness/subscription_form.html', {'success': True})
    else:
        return redirect('login')  # You may want to customize this redirection


def rate_workout_plan(request, plan_id):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        plan = WorkoutPlan.objects.get(id=plan_id)
        Rating.objects.create(
            user=request.user, workout_plan=plan, rating=rating_value)
        return render(request, 'fitness/rating_form.html', {'success': True})
    else:
        return render(request, 'fitness/rating_form.html', {'plan_id': plan_id})


def subscribe_free_trial(request):
    # Your logic for handling free trial subscription
    return render(request, 'fitness/subscribe_free_trial.html')
