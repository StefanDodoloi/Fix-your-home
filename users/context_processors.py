from django.contrib.auth.models import User

def user_profile(request):
    return {
        'logged_in_user': request.user
    }
